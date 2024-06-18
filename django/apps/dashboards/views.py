from django.shortcuts import render
import psycopg2
import pandas.io.sql as sqlio
import pandas as pd
import datetime as dt
import collections
import os

def get_kpis(
        data: pd.Series
):
    def momentum(
            new: float,
            old: float
    ):
        return (new - old) / abs(old)

    return {
        "value": round(data.iloc[0], 3),
        "momentum": round(momentum(
            data.iloc[-1], data.iloc[0]), 3),
        "volatility": round(data.std(), 3),
        "skewness": round(data.skew(), 3),
        "kurtosis": round(data.kurt(), 3)}


def home(request):
    print(request.user)
    return render(request, 'dashboards/home.html')


def fg(request):
    # Connecting to Aws-Rds-PostgreSQL
    conn = psycopg2.connect(
        database=os.getenv("SQL_DB"),
        user=os.getenv("SQL_USER"),
        password=os.getenv("SQL_PASSWORD"),
        host=os.getenv("SQL_HOST"),
        port=os.getenv("SQL_PORT")
    )
    data = sqlio.read_sql_query('SELECT * FROM "financial_indexes"', conn).rename(
        columns={"datetime":"date", "fear_greed_index_nasdaq":"nasdaq", "fear_greed_index_nyse":"nyse"})
    context = dict()
    times = ["(24H)", "(7D)", "(1M)", "(3M)", "(6M)", "(1Y)"]
    for market in ["nyse", "nasdaq"]:
        l = [get_kpis(data[data["date"] >= (
                data["date"].iloc[-1] - dt.timedelta(days=delta))][market]) \
             for delta in [1, 7, 30, 90, 180, 365]]
        dd = collections.defaultdict(list)
        for sd in l:
            for key in sd.keys():
                dd[key].append(sd[key])
        dd["time"] = times
        context[f"{market}_kpis"] = zip(dd["time"], dd["value"], dd["momentum"],
            dd["volatility"], dd["skewness"], dd["kurtosis"])

    context["dates"] = [x.strftime("%d.%m.%Y") for x in data.date][-2000:]
    context["nyse"] = [round(float(x), 2) for x in data['nyse'].tolist()[-2000:]]
    context["nasdaq"] = [round(float(x), 2) for x in data['nasdaq'].tolist()[-2000:]]

    # Closing connection to Aws-Rds-PostgreSQL
    conn.close()

    return render(request, 'dashboards/fg.html', context)


