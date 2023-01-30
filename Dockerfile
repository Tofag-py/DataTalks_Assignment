
FROM python:3.9

RUN apt-get install wget
RUN pip install pandas psycopg2 sqlalchemy

WORKDIR /app

COPY Ingest_data.py Ingest_data.py

ENTRYPOINT ["bash", "Ingest_data.py"]