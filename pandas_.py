import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="    ")

cur = conn.cursor()

cur.execute('SELECT customer.first_name,customer.last_name, country.country'
            ' FROM customer INNER JOIN address ON customer.address_id = address.address_id '
            'INNER JOIN city ON address.city_id = city.city_id '
            'INNER JOIN country ON city.country_id = country.country_id')


customer = cur.fetchall()
df=pd.DataFrame(customer)
df.columns=['first_name','second_name','country']

df1=df.loc[df['country'].isin(['India','Egypt','Kuwait'])]
print(df1)
cur.close()




