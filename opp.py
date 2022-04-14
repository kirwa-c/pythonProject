import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sqlalchemy import create_engine as ce

import psycopg2




"""connection to the DataBase"""
con = psycopg2.connect(
    host="127.0.0.1",
    database="dvdrental",
    user="postgres",
    password="    ",
    port="5432")

# cursor
# cur = con.cursor()
# print(con)
# """execute query to output customer_name, address, email"""
#
# cur.execute("select first_name, last_name, address_id from customer")
#
# results = cur.fetchall()
# # print(results)
# cur.execute(f"select city_id, address_id from address where address_id = {'address_id'}")
# add=cur.fetchall()
#
# # print(add)
# cur.execute(f"select city_id, country_id from city where city_id = {'city_id'}")
# city=cur.fetchall()
#
# # print(city)
# cur.execute(f"select country from country")
# country=cur.fetchall()
#
# # print(country)

