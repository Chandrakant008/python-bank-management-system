from register import *
from bank import *

status = False


print("Wellcome chandra kant in your Banking Project")
while True:
    try:
        register = int(input("1. SignUp\n"
                         "2. SignIn"))
        if register == 1 or register == 2:
            if register  == 1:
                signup()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter valid Input From Options")

    except ValueError :
        print("Invalid Input Try Again with Numbers")


result = db_query("SHOW TABLES;")
print("Tables in DB:", result)

# account_number = db_query(f"SELECT account_number FROM customer WHERE username = '{user}';")
account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")



while status:
    print(f"Welcome{user.capitalize()} choose your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                         "2. Cash Deposit\n"
                         "3. Cash Withdrawal\n"
                         "4. Fund Transfer\n"
                         ))
        if facility >= 1 or facility <= 4:


            if facility  == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceenquiry()
                pass
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()

                        break
                    except ValueError:
                         print("Enter valid Input ie. Number")
                         continue

            elif facility == 3:
                while True:
                    try:
                       amount = int(input("Enter Amount to Withdraw"))
                       bobj = Bank(user, account_number[0][0])
                       bobj.withdraw(amount)
                       mydb.commit()

                       break
                    except ValueError :
                        print("Enter valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount =  int(input("Enter money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()

                        break
                    except ValueError :
                        print("Enter valid Input ie. Number")
                        continue
        else:
            print("Please Enter valid Input From Options")
            continue


    except ValueError :
        print("Invalid Input Try Again with Numbers")
        continue










