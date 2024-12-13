import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="bank_users"
)
print(connection)
mycursor=connection.cursor()
#mycursor.execute("create database bank_users")
#mycursor.execute("create table details(name varchar(30),gender varchar(20),age int,city varchar(30),state varchar(30),pin int,account_number bigint,balance bigint)")
#mycursor.execute('ALTER TABLE details ADD COLUMN total_balance bigint') 
#mycursor.execute('DELETE FROM customer where name="piyush"')
#mycursor.execute('delete from customers where name="piyush"')
#mycursor.execute("DELETE FROM details WHERE name = %s;", ('piyush',))

import numpy as np
import random
def main():
    while True:
        print("WELCOME")
        print("please select option")
        print("1.create new account")
        print("2. check exsiting account")
        print("3. exit ")
        n=int(input("enter your option 1,2,3"))
        if n==1:
            new_user()
        elif n==2:
            check_details()
        elif n==3:
            print("thankyou")
            break
        else:
            print("please selelct from menu")


def new_user():
    print("WELCOME TO BANK")  
    print("Please Enter your deatils ")
    a=input("enter your name")
    b=input("enter your gender")
    c=int(input("enter your age"))
    d=input("enter your city") 
    e=input("enter your state")
    f=int(input("create 6 digit pin")) 
    g=random.randint(10000000000,99999999999)
    h=0
    total=0
    mycursor.execute("insert into details(name,gender,age,city,state,pin,account_number,balance,total_balance) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);", (a,b,c,d,e,f,g,h,total))

def check_details():
    print("Please enter your account details.")
    name=input("enter your name")
    p=int(input("enter you pin"))
    mycursor.execute("select * from details where name= %s AND pin= %s;", (name, p))    
    result=mycursor.fetchone()
    if result:
        #print(f"\nAccount Details for Account Number: {account_number}")
        account_number = result[6]
        print(f"Name: {result[0]}")
        print(f"Gender: {result[1]}")
        print(f"Age: {result[2]}")
        print(f"City: {result[3]}")
        print(f"State: {result[4]}")
        print(f"Balance: {result[7]}")
        print(f"Total Balance: {result[8]}")
        action = int(input("\nDo you want to deposit(1) or withdraw money(2)? (deposit=1/withdraw=2/):"))
        
        if action == 1:
           deposit(result,account_number)
        elif action == 2:
           withdraw(result,account_number)
        else:
            print("No action taken.")
    else:
        print("Account not found or invalid pin.")

def deposit(result,account_number):
    money=int(input("enter your amount"))
    if money>0:
        current_balance = result[7]
        current_total_balance=result[8]

        new1=current_balance+ money
        new2=current_total_balance + money
        mycursor.execute("UPDATE details SET balance = %s, total_balance = %s WHERE account_number = %s;", 
                         (new1,new2,account_number)) 
        connection.commit()

def withdraw(result,account_number):
    money=int(input("enter amount you want to withdraw"))
    current_balance = result[7]
    current_total_balance = result[8]
    if money <= 0:
        print("Invalid amount. Withdrawal must be greater than 0.")
    elif money > current_balance:
        print("Insufficient balance.")
    else:
        new1 =current_balance - money
        new2= current_total_balance - money
        mycursor.execute("update details set balance= %s , total_balance= %s where account_number=%s;",
                         (new1,new2,account_number))
        connection.commit()
main()










































connection.commit()
