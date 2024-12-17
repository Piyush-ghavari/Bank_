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

        # Fullscreen and background
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#3b5998")  # Background color (blue)

        # Show login screen initially
        self.show_login_screen()

    def clear_screen(self):
        """Clears the screen for navigation between pages."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        """Creates the login screen."""
        self.clear_screen()
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login form
        tk.Label(frame, text="Name:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=0, column=0, pady=10)
        self.entry_name = tk.Entry(frame, font=("Arial", 14))
        self.entry_name.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Pin:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=1, column=0, pady=10)
        self.entry_pin = tk.Entry(frame, show="*", font=("Arial", 14))
        self.entry_pin.grid(row=1, column=1, pady=10)

        tk.Button(frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Create New Account", font=("Arial", 14), bg="#FF6347", fg="white", command=self.create_account_screen).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Exit", font=("Arial", 14), bg="#FF4500", fg="white", command=self.root.quit).grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        """Logs in the user."""
        name = self.entry_name.get()
        pin = self.entry_pin.get()

        if name and pin.isdigit():
            mycursor.execute("SELECT * FROM details WHERE name = %s AND pin = %s", (name, int(pin)))
            result = mycursor.fetchone()

            if result:
                self.current_account = result
                self.show_account_details()
            else:
                messagebox.showerror("Login Failed", "Invalid Name or Pin")
        else:
            messagebox.showerror("Input Error", "Please enter valid name and numeric pin.")

    def create_account_screen(self):
        """Shows the account creation form."""
        self.clear_screen()
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Name:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=0, column=0, pady=10)
        self.entry_new_name = tk.Entry(frame, font=("Arial", 14))
        self.entry_new_name.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Gender:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=1, column=0, pady=10)
        self.entry_new_gender = tk.Entry(frame, font=("Arial", 14))
        self.entry_new_gender.grid(row=1, column=1, pady=10)

        tk.Label(frame, text="Age:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=2, column=0, pady=10)
        self.entry_new_age = tk.Entry(frame, font=("Arial", 14))
        self.entry_new_age.grid(row=2, column=1, pady=10)

        tk.Label(frame, text="City:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=3, column=0, pady=10)
        self.entry_new_city = tk.Entry(frame, font=("Arial", 14))
        self.entry_new_city.grid(row=3, column=1, pady=10)

        tk.Label(frame, text="State:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=4, column=0, pady=10)
        self.entry_new_state = tk.Entry(frame, font=("Arial", 14))
        self.entry_new_state.grid(row=4, column=1, pady=10)

        tk.Label(frame, text="Pin:", font=("Arial", 14), bg="#3b5998", fg="white").grid(row=5, column=0, pady=10)
        self.entry_new_pin = tk.Entry(frame, font=("Arial", 14), show="*")
        self.entry_new_pin.grid(row=5, column=1, pady=10)

        tk.Button(frame, text="Create Account", font=("Arial", 14), bg="#FF6347", fg="white", command=self.create_account).grid(row=6, column=0, columnspan=2, pady=20)
        tk.Button(frame, text="Back", font=("Arial", 14), bg="#4682B4", fg="white", command=self.show_login_screen).grid(row=7, column=0, columnspan=2, pady=10)

    def create_account(self):
        """Creates a new account."""
        name = self.entry_new_name.get()
        gender = self.entry_new_gender.get()
        age = self.entry_new_age.get()
        city = self.entry_new_city.get()
        state = self.entry_new_state.get()
        pin = self.entry_new_pin.get()

        if name and gender and age.isdigit() and city and state and pin.isdigit():
            account_number = random.randint(10000000000, 99999999999)
            mycursor.execute(
                "INSERT INTO details(name, gender, age, city, state, pin, account_number, balance, total_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (name, gender, int(age), city, state, int(pin), account_number, 0, 0)
            )
            connection.commit()
            messagebox.showinfo("Success", "Account created successfully.")
            self.show_login_screen()
        else:
            messagebox.showerror("Input Error", "All fields are required and must be valid.")

    def show_account_details(self):
        """Displays the user's account details."""
        self.clear_screen()
        frame = tk.Frame(self.root, bg="#3b5998")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Display all account details
        tk.Label(frame, text=f"Name: {self.current_account[0]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=0, column=0, pady=10, sticky="w")
        tk.Label(frame, text=f"Gender: {self.current_account[1]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=1, column=0, pady=10, sticky="w")
        tk.Label(frame, text=f"Age: {self.current_account[2]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=2, column=0, pady=10, sticky="w")
        tk.Label(frame, text=f"City: {self.current_account[3]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=3, column=0, pady=10, sticky="w")
        tk.Label(frame, text=f"State: {self.current_account[4]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=4, column=0, pady=10, sticky="w")
        tk.Label(frame, text=f"Balance: {self.current_account[7]}", bg="#3b5998", fg="white", font=("Arial", 16)).grid(row=5, column=0, pady=10, sticky="w")

        # Actions
        tk.Button(frame, text="Deposit", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.deposit).grid(row=6, column=0, pady=10)
        tk.Button(frame, text="Withdraw", font=("Arial", 14), bg="#FF6347", fg="white", command=self.withdraw).grid(row=7, column=0, pady=10)
        tk.Button(frame, text="Delete Account", font=("Arial", 14), bg="#FF0000", fg="white", command=self.delete_account).grid(row=8, column=0, pady=10)
        tk.Button(frame, text="Logout", font=("Arial", 14), bg="#4682B4", fg="white", command=self.show_login_screen).grid(row=9, column=0, pady=10)

    def deposit(self):
        """Deposits money to the user's account."""
        amount = self.get_amount("deposit")
        if amount:
            new_balance = self.current_account[7] + amount
            mycursor.execute("UPDATE details SET balance = %s WHERE name = %s AND pin = %s", (new_balance, self.current_account[0], self.current_account[5]))
            connection.commit()
            self.current_account = (*self.current_account[:7], new_balance, self.current_account[8])
            messagebox.showinfo("Success", f"Deposited {amount} successfully.")
            self.show_account_details()

    def withdraw(self):
        """Withdraws money from the user's account."""
        amount = self.get_amount("withdraw")
        if amount and amount <= self.current_account[7]:
            new_balance = self.current_account[7] - amount
            mycursor.execute("UPDATE details SET balance = %s WHERE name = %s AND pin = %s", (new_balance, self.current_account[0], self.current_account[5]))
            connection.commit()
            self.current_account = (*self.current_account[:7], new_balance, self.current_account[8])
            messagebox.showinfo("Success", f"Withdrawn {amount} successfully.")
            self.show_account_details()
        elif amount:
            messagebox.showerror("Error", "Insufficient funds.")

    def delete_account(self):
        """Deletes the user's account."""
        confirm = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account?")
        if confirm:
            mycursor.execute("DELETE FROM details WHERE name = %s AND pin = %s", (self.current_account[0], self.current_account[5]))
            connection.commit()
            self.current_account = None
            messagebox.showinfo("Deleted", "Account deleted successfully.")
            self.show_login_screen()

    def get_amount(self, action):
        """Prompts the user for an amount."""
        try:
            amount = simpledialog.askfloat(f"{action.capitalize()} Amount", f"Enter amount to {action}:")
            if amount and amount > 0:
                return amount
            raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")
            return None


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
