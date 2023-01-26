#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    url1 = params.url1
    url2 = params.url2
    table_name = params.table_name

    first_file = "output1.csv"
    second_file = "output2.csv"

    os.system(f"wget {url1} -O {first_file}")

    os.system(f"wget {url2} -O {second_file}")

    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(first_file, iterator=True, chunksize=50000)
    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists="append")

    while True:
        t_start = time()
        df = next(df_iter)
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print("Another chunk inserted..., took %.3f second" % (t_end - t_start))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import Data into the Postgres database')


    parser.add_argument('user', help='username for postgres')
    parser.add_argument('password', help='pasword for postgres')
    parser.add_argument('host', help='host for postgres')
    parser.add_argument('port', help='port for postgres')
    parser.add_argument('db', help='Database Name')
    parser.add_argument('table_name', help='Database name for postgres')
    parser.add_argument('url1', help='location of file 1')
    parser.add_argument('url2', help='location of file2')


    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    main(args)
