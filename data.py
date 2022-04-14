import psycopg2

"""connection to the DataBase"""
con = psycopg2.connect(
    host="127.0.0.1",
    database="dvdrental",
    user="postgres",
    password="    ",
    port="5432")
# cursor
cur = con.cursor()

"""execute query to output customer_name, address, email"""

cur.execute("select first_name, last_name, address_id, email, customer_id from customer")

results = cur.fetchall()

# print(results)

def payment(customer_id):
    pay_list = []
    """execute query to output customer_id_1, staff_id, rental_id"""
    cur.execute(f"select customer_id, staff_id, rental_id from payment where customer_id = {customer_id}")

    pay = cur.fetchall()
    # print(pay)

    for j in pay:
        pay_dict = {}
        pay_dict['customer_id'] = j[0]
        pay_dict['staff_id'] = j[1]
        pay_dict['rental_id'] = j[2]
        pay_list.append(pay_dict)
    # print(pay_list)
    return pay_list
    print(pay_list)
#

customer_list = []
for customer in results[:1]:
    # print(customer)
    combined_dict = {}
    combined_dict['customer name'] = customer[0] + ' ' + customer[1]
    combined_dict['address'] = customer[2]
    combined_dict['email'] = customer[3]
    """execute query to output inventory_id"""
    cur.execute(f"select inventory_id from rental where rental_id = {customer[4]}")


    try:
        inventory_id = cur.fetchall()[0][0]
        cur.execute(f"select film_id from inventory where inventory_id = {inventory_id}")
        film_id = cur.fetchall()
        # print(inventory_id)

    # print(inventory_id)


    # cur.execute(f"select film_id from inventory where inventory_id = {inventory_id}")
    # film_id = cur.fetchall()
    # print(film_id)

        cur.execute(f"select title, description, rental_duration from film where film_id = {film_id[0][0]}")
        sects = cur.fetchall()
        print(sects)
        film_sect = {}
        film_sect['title'] = sects[0][0]
        film_sect['description'] = sects[0][1]
        film_sect['rental_duration'] = sects[0][2]

        cur.execute(f"SELECT address_id FROM public.address where address_id = {customer[2]};")
        add = cur.fetchall()[0][0]
        cur.execute(f"SELECT store_id, manager_staff_id FROM public.store where address_id = '{add}';")
        store = cur.fetchall()
        # print(store)


        combined_dict['film_section'] = film_sect
        combined_dict['payment'] = payment(customer_id=customer[4])

    except IndexError:
        print(customer)
    # print(combined_dict)

    customer_list.append(combined_dict)

# print(customer_list)