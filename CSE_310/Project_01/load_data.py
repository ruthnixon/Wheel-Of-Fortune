import sqlite3
import datetime

### These lines connect us to the database and create an object that can run sql commands.

con = sqlite3.connect('CSE_310\sqlite-tools-win32-x86-3360000\Project_01.db')
cur = con.cursor()

### This program creates the tables for the database.

# ThiS code will create a customer table  
#cur.execute('''CREATE TABLE customer
#               (customer_id, full_name, date_joined, country_code, phone_number)''')

# ThiS code will create a product table
#cur.execute('''CREATE TABLE product
#               (product_id, product_name, product_price)''')

# ThiS code will create an order table
#cur.execute('''CREATE TABLE customer_orders
#               (order_number, product_code, item_name, order_date, customer_id)''')

### The code below creates some entries for the customers and products tables.

#customers = [(1234,'Genete Begede', datetime.datetime.now()-datetime.timedelta(days=30), '+251', '801-555-5555'),
#            (2324, 'Sishma Shebushe', datetime.datetime.now()-datetime.timedelta(days=28), '+34', '233-573-0001'),
#            (7843, 'John Clark', datetime.datetime.now()-datetime.timedelta(days=26), '+24', '662-372-1200'),
#            (9020, 'George Washington', datetime.datetime.now()-datetime.timedelta(days=20), '+1', '704-245-1776'),
#            (8932, 'Robert Robertson', datetime.datetime.now()-datetime.timedelta(days=18), '+222', '560-798-4682'),
#            (3012, 'Bart Simpson', datetime.datetime.now()-datetime.timedelta(days=12), '+33', '742-706-1989')]
#
#products = [(123,'sugar', '$2.99'),
#            (244,'tomato', '$0.89'),
#            (786,'pasta', '$1.00')]

#cur.executemany('INSERT INTO customer VALUES (?,?,?,?,?)', customers)
#cur.executemany('INSERT INTO  product VALUES (?,?,?)', products)

### I would use this line of code to empty the tables if I had an issue with the data. 

#cur.execute('DELETE FROM product')

con.commit()
con.close()