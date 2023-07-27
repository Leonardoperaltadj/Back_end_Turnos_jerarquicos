import psycopg2
from psycopg2 import DatabaseError
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()

db = SQLAlchemy()

host=os.environ['PGSQL_HOST']
port=os.environ['PGSQL_PORT']
user=os.environ['PGSQL_USER']
password=os.environ['PGSQL_PASSWORD']
database=os.environ['PGSQL_DATABASE']

DATEBASE_CONNECTION_URI= f'postgresql://{user}:{password}@{host}:{port}/{database}'

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            port=config('PGSQL_PORT'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex