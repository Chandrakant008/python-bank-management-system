# User Registration Signin Signup

from database import *
from customer import *
from bank import Bank
import random


def signup():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print(" Username already exists. Try again. ")
        signup()
    else:
        print("Username is available. Proceed with registration.")
        password = input("Enter Your Password: ")
        name = input("Enter your Name: ")
        age = input("Enter your Age : ")
        city  = input("Enter your City : ")
        while True :
            # account_number = generate_unique_account_number()
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}'; ")
            if temp:
                continue
            else:
                print("Your  Account Number", account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
# signup()


def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Your  Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            #print (temp[0][0])
            if temp[0][0] == password:
                print("Sign In Sucessfully")
                return username
            else:
                print("You entered the wrong password. Please try again ")
                continue

    else:
        print("Please Enter Correct Username")
        SignIn()


