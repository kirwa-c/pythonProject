import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="    ")
cur = conn.cursor()


cur.execute('SELECT customer.first_name,customer.last_name, payment.amount'
            ' FROM customer inner JOIN payment ON payment.customer_id = payment.customer_id')


payment = cur.fetchall()
df=pd.DataFrame(payment)
print(df)


cur.close()