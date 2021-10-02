"""
CSE 110 
BYU-Idaho 
Author: Rute Berehe 
Module#1

"""
import sqlite3
import datetime

### The main function connects us to the database and runs a while loop which will allow us to call certain functions to executes sql queries. 

def main():

    ### Here we are connecting to the database and creating the cursor object. 

    con = sqlite3.connect('CSE_310\sqlite-tools-win32-x86-3360000\Project_01.db')
    cur = con.cursor()
    running = True 

    ### In this we are looping to recieve different commands from the user. 

    while running:
        print("Please select one of the following: ") 
        print("N. New Order")
        print("S. Search Order")
        print("D. Delete Order")
        print("E. Edit Order")
        print("Q. Quit")

        choice = input("").lower()

        ### The if statments below call certain functions depending on the option the users selected. 
         
        if choice == "n":
            enter_order(cur,con)
        elif choice == "s":
            search_order(cur,con)
        elif choice == "d":
            delete_order(cur, con)
        elif choice == "e":
            edit_order(cur, con)
        elif choice == "q":
            running = False
        
    con.commit()
    con.close()

### This function allows the user to insert a new entry to the customer_orders table. 

def enter_order(cur,con):
    order_number = input("What is the order number? ")
    product_code = input("What is the product code? ")
    customer_id = input("What is the customer ID? ")
    item_name = input("What is the name of the item? ")
    order_date = datetime.datetime.now()

### The execute function allows to run sql commands. Its first parameter is the query itself. 
### There are question marks in it which get replaced by the data in the second argumnet which is stored in a tuple. 

    cur.execute('''INSERT INTO customer_orders VALUES (?,?,?,?,?)''', (order_number, product_code, item_name, order_date, customer_id))
    print("Order Entered")
    con.commit()

### This function allows the user to retrive data. 

def search_order(cur,con):
    order_number = input("Please enter the order number. ")

### The query performs a join on the customer_orders and the customer table.
### The cur.fetchall() function will return the data retrived from the select statment.

    cur.execute('''SELECT customer.full_name, customer_orders.order_date, customer_orders.product_code FROM customer JOIN customer_orders ON customer.customer_id = customer_orders.customer_id WHERE customer_orders.order_number = ?''', (order_number))
    print(cur.fetchall())
    con.commit()

### This function allow us to delete the table entry given the order number. 

def delete_order(cur, con):
    delete_number = input("Please enter the order number of the order you would like to delete. ")

    cur.execute('''DELETE FROM customer_orders WHERE order_number = ?''', (delete_number))
    print("Order Deleted. ")
    con.commit()

### This function allow us to modify the table given the order number.

def edit_order(cur, con):
    edit_number = input("Please enter the order number you would like to edit. ")

    product_code = input("What is the product code? ")
    customer_id = input("What is the customer ID? ")
    item_name = input("What is the name of the item? ")

    cur.execute('''UPDATE customer_orders SET product_code = ?, item_name = ?, customer_id = ? WHERE order_number = ? ''', (product_code, item_name, customer_id, edit_number))
    print("Order Updated. ")
    con.commit()

main()