# pull official base image
FROM python:3.9.6-slim

# set work directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Copy requirements and Install (pip)
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy ./django to /usr/src/app/
COPY . .

# Copy entrypoint.sh and execute with Shell
COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
