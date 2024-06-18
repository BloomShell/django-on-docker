from django.shortcuts import render
import psycopg2
import pandas.io.sql as sqlio
import pandas as pd
import datetime as dt
import collections
import os


def home(request):
    print(request.user)
    return render(request, 'projects/home.html')


def convsec(request):
    return render(request, 'projects/convsec.html')


def beecell(request):
    conn = psycopg2.connect(
        database=os.getenv("SQL_DB"),
        user=os.getenv("SQL_USER"),
        password=os.getenv("SQL_PASSWORD"),
        host=os.getenv("SQL_HOST"),
        port=os.getenv("SQL_PORT")
    )
    data = sqlio.read_sql_query("SELECT * FROM beecell_performance", conn).rename(
        columns={"datetime": "date", "beecell_returns": "beecell", "spy_returns": "spy"})
    context = dict()
    context["dates"] = [x.strftime("%d.%m.%Y") for x in data.date]
    context["beecell"] = data.beecell.round(5).tolist()
    context["spy"] = data.spy.round(5).tolist()
    beecell_composition = sqlio.read_sql_query("SELECT * FROM beecell_composition", conn).sort_values("weight", ascending=False)
    beecell_composition["weight"] = beecell_composition["weight"].round(5)
    context["beecell_comp"] = zip(
        beecell_composition["name"].tolist(),
        beecell_composition["symbol"].tolist(),
        beecell_composition["weight"].tolist(),
        beecell_composition["market_cap"].tolist(),
        beecell_composition["sector"].tolist(),
        beecell_composition["industry"].tolist()
    )
    conn.close()
    return render(request, 'projects/beecell.html', context)
