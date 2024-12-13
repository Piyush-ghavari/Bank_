import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="bank_users"
)
mycursor = connection.cursor()

# Main Application Class
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.current_account = None  # Holds the logged-in account details

        # Make the window full-screen
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#3b5998")  # Background color (blue)

        # Start by showing the login screen
        self.show_login_screen()

    def show_login_screen(self):
        """Creates the login screen."""
        self.clear_screen()

        # Centering widgets
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login form
        self.label_name = tk.Label(frame, text="Name:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_name.grid(row=0, column=0, pady=10, padx=10)
        self.entry_name = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_name.grid(row=0, column=1, pady=10)

        self.label_pin = tk.Label(frame, text="Pin:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_pin.grid(row=1, column=0, pady=10, padx=10)
        self.entry_pin = tk.Entry(frame, show="*", font=("Arial", 14), width=30)
        self.entry_pin.grid(row=1, column=1, pady=10)

        self.btn_login = tk.Button(frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_create_account = tk.Button(frame, text="Create New Account", font=("Arial", 14), bg="#FF6347", fg="white", command=self.create_account_screen)
        self.btn_create_account.grid(row=3, column=0, columnspan=2, pady=10)

        self.btn_exit = tk.Button(frame, text="Exit", font=("Arial", 14), bg="#FF4500", fg="white", command=self.root.quit)
        self.btn_exit.grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        """Logs in the user."""
        name = self.entry_name.get()
        pin = int(self.entry_pin.get())

        if name and pin:
            mycursor.execute("SELECT * FROM details WHERE name = %s AND pin = %s", (name, pin))
            result = mycursor.fetchone()

            if result:
                self.current_account = result  # Store the account details for later use
                self.show_account_details()
            else:
                messagebox.showerror("Login Failed", "Invalid Name or Pin")
        else:
            messagebox.showerror("Input Error", "Please enter both name and pin.")

    def create_account_screen(self):
        """Shows the create account form."""
        self.clear_screen()

        # Centering widgets
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label_new_name = tk.Label(frame, text="Name:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_name.grid(row=0, column=0, pady=10, padx=10)
        self.entry_new_name = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_new_name.grid(row=0, column=1, pady=10)

        self.label_new_gender = tk.Label(frame, text="Gender:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_gender.grid(row=1, column=0, pady=10, padx=10)
        self.entry_new_gender = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_new_gender.grid(row=1, column=1, pady=10)

        self.label_new_age = tk.Label(frame, text="Age:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_age.grid(row=2, column=0, pady=10, padx=10)
        self.entry_new_age = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_new_age.grid(row=2, column=1, pady=10)

        self.label_new_city = tk.Label(frame, text="City:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_city.grid(row=3, column=0, pady=10, padx=10)
        self.entry_new_city = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_new_city.grid(row=3, column=1, pady=10)

        self.label_new_state = tk.Label(frame, text="State:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_state.grid(row=4, column=0, pady=10, padx=10)
        self.entry_new_state = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_new_state.grid(row=4, column=1, pady=10)

        self.label_new_pin = tk.Label(frame, text="Pin:", fg="white", bg="#3b5998", font=("Arial", 14))
        self.label_new_pin.grid(row=5, column=0, pady=10, padx=10)
        self.entry_new_pin = tk.Entry(frame, show="*", font=("Arial", 14), width=30)
        self.entry_new_pin.grid(row=5, column=1, pady=10)

        self.btn_create = tk.Button(frame, text="Create Account", font=("Arial", 14), bg="#FF6347", fg="white", command=self.create_account)
        self.btn_create.grid(row=6, column=0, columnspan=2, pady=20)

        self.btn_exit = tk.Button(frame, text="Exit", font=("Arial", 14), bg="#FF4500", fg="white", command=self.root.quit)
        self.btn_exit.grid(row=7, column=0, columnspan=2, pady=10)

    def create_account(self):
        """Creates a new account."""
        name = self.entry_new_name.get()
        gender = self.entry_new_gender.get()
        age = int(self.entry_new_age.get())
        city = self.entry_new_city.get()
        state = self.entry_new_state.get()
        pin = int(self.entry_new_pin.get())
        
        if name and gender and city and state and pin and age:
            account_number = random.randint(10000000000, 99999999999)
            balance = 0
            total_balance = 0

            # Insert into the database
            mycursor.execute(
                "INSERT INTO details(name, gender, age, city, state, pin, account_number, balance, total_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (name, gender, age, city, state, pin, account_number, balance, total_balance)
            )
            connection.commit()

            messagebox.showinfo("Account Created", "Your account has been successfully created!")
            self.show_login_screen()
        else:
            messagebox.showerror("Input Error", "Please fill in all the fields.")

    def show_account_details(self):
        """Displays the account details after login."""
        self.clear_screen()

        # Centering widgets
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        name = self.current_account[0]
        gender = self.current_account[1]
        age = self.current_account[2]
        city = self.current_account[3]
        state = self.current_account[4]
        balance = self.current_account[7]
        total_balance = self.current_account[8]

        # Show details
        tk.Label(frame, text=f"Name: {name}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=0, column=0, pady=10)
        tk.Label(frame, text=f"Gender: {gender}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=1, column=0, pady=10)
        tk.Label(frame, text=f"Age: {age}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=2, column=0, pady=10)
        tk.Label(frame, text=f"City: {city}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=3, column=0, pady=10)
        tk.Label(frame, text=f"State: {state}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=4, column=0, pady=10)
        tk.Label(frame, text=f"Balance: {balance}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=5, column=0, pady=10)
        tk.Label(frame, text=f"Total Balance: {total_balance}", fg="white", bg="#3b5998", font=("Arial", 16)).grid(row=6, column=0, pady=10)

        # Deposit and Withdraw Buttons
        self.btn_deposit = tk.Button(frame, text="Deposit", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.deposit)
        self.btn_deposit.grid(row=7, column=0, pady=20)

        self.btn_withdraw = tk.Button(frame, text="Withdraw", font=("Arial", 14), bg="#FF6347", fg="white", command=self.withdraw)
        self.btn_withdraw.grid(row=8, column=0, pady=10)

        self.btn_exit = tk.Button(frame, text="Exit", font=("Arial", 14), bg="#FF4500", fg="white", command=self.root.quit)
        self.btn_exit.grid(row=9, column=0, pady=10)

    def deposit(self):
        """Handles deposit functionality."""
        money = self.get_transaction_amount("deposit")
        if money > 0:
            current_balance = self.current_account[7]
            current_total_balance = self.current_account[8]
            account_number = self.current_account[6]

            new_balance = current_balance + money
            new_total_balance = current_total_balance + money

            mycursor.execute(
                "UPDATE details SET balance = %s, total_balance = %s WHERE account_number = %s;",
                (new_balance, new_total_balance, account_number)
            )
            connection.commit()
            messagebox.showinfo("Deposit Successful", f"You have deposited {money}. New Balance: {new_balance}")

    def withdraw(self):
        """Handles withdrawal functionality."""
        money = self.get_transaction_amount("withdraw")
        if money > 0:
            current_balance = self.current_account[7]
            if money <= current_balance:
                current_total_balance = self.current_account[8]
                account_number = self.current_account[6]

                new_balance = current_balance - money
                new_total_balance = current_total_balance - money

                mycursor.execute(
                    "UPDATE details SET balance = %s, total_balance = %s WHERE account_number = %s;",
                    (new_balance, new_total_balance, account_number)
                )
                connection.commit()
                messagebox.showinfo("Withdrawal Successful", f"You have withdrawn {money}. New Balance: {new_balance}")
            else:
                messagebox.showerror("Insufficient Balance", "You do not have enough funds to withdraw this amount.")

    def get_transaction_amount(self, transaction_type):
        """Gets the transaction amount for deposit or withdraw."""
        amount = simpledialog.askinteger("Enter Amount", f"Enter the amount you want to {transaction_type}:")
        return amount if amount is not None and amount > 0 else 0

    def clear_screen(self):
        """Clears the current screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

# Start the GUI application
root = tk.Tk()
app = BankApp(root)
root.mainloop()
