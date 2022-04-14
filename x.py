# Example python program to read data from a PostgreSQL table

# and load into a pandas DataFrame

import psycopg2

import pandas as pds

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as st
def get_engine(user,password,host,db):
    url= f"postgresql://(user):(password)0(host):port/(db)"
    if not database_exists(url):
        create_database(url)
    engine create_engine(url)

# Create an engine instance

alchemyEngine = create_engine('postgresql+psycopg2://test:@127.0.0.1', pool_recycle=3600);

# Connect to PostgreSQL server

dbConnection = alchemyEngine.connect();

# Read data from PostgreSQL database table and load into a DataFrame instance

df = pds.read_sql("select * from \"dvdrental\"", dbConnection);

pds.set_option('display.expand_frame_repr', False);

# Print the DataFrame

print(df);

# Close the database connection

dbConnection.close();