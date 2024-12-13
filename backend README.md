# Bank System

## Overview

This is a simple banking system built using Python and MySQL. It allows users to create new accounts, check their existing account details, deposit money, and withdraw money. The system uses a MySQL database to store and manage user data.

### Features:
- **Create a New Account**: Users can create an account by entering their personal details (name, gender, age, city, state, and a 6-digit pin).
- **Check Existing Account**: Users can check their account details by entering their name and pin.
- **Deposit Money**: Users can deposit money into their account.
- **Withdraw Money**: Users can withdraw money from their account, ensuring that they have sufficient balance.

### Technologies Used:
- Python 3.x
- MySQL Database
- `mysql-connector` for MySQL interaction
- `numpy` for random number generation (used for account number generation)

## Setup Instructions

### Prerequisites
- Python 3.x installed
- MySQL Server installed and running
- Install required Python libraries:
  - `mysql-connector`
  - `numpy`

### Step-by-Step Installation

1. **Install Python Libraries**:
   Open your terminal or command prompt and run the following commands to install the required libraries:

   ```bash
   pip install mysql-connector numpy
2. **Set Up MySQL Database: Ensure MySQL is running, then log into MySQL and run the following commands to set up the database and table:**
     CREATE DATABASE bank_users;

  USE bank_users;


    CREATE TABLE details 
  
    (
  
    name VARCHAR(30),
    
    gender VARCHAR(20),
    
    age INT,
    
    city VARCHAR(30),
    
    state VARCHAR(30),
    
    pin INT,
    
    account_number BIGINT,
    
    balance BIGINT,
    
    total_balance BIGINT
    
    );

3. **Running the Python Script: Once the database and table are set up, you can run the Python script to start the banking system:**
   
   ```bash
    python bank_system.py

## How to Use:
**Create a New Account:**

- Select option 1 from the menu to create a new account.
- Enter your personal details (name, gender, age, city, state, and a 6-digit pin).
- 
**Check Existing Account:**

- Select option 2 to view your account details.
- Enter your name and PIN to access your account.
- You can then choose to deposit or withdraw money.**
- 
**Exit:**

- Select option 3 to exit the application.

## Screenshots
1. Home Screen
   This is the main menu screen where users can choose to create a new account, check existing account details, or exit.


![Screenshot 2024-12-13 204129](https://github.com/user-attachments/assets/79b6b209-e8a9-4f3c-90aa-73fc8f2cb9ae)


2. New Account Creation
    This screen appears when the user opts to create a new account. It prompts the user for their personal information.


![Screenshot 2024-12-13 204921](https://github.com/user-attachments/assets/f67b0dd1-7e3a-497b-b2de-5555d7ad35ec)


3. Account Details with deposit and withdrawl
  Once the user enters their name and pin, they can view their account details here.

![Screenshot 2024-12-13 205313](https://github.com/user-attachments/assets/06efc85d-1c30-4a64-8eee-6e665721265a)


4. Deposit Money and Withdraw Money
   This screen is shown when the user chooses to deposit money into their account.
   Users can withdraw money from their account using this screen.

   ![Screenshot 2024-12-13 210020](https://github.com/user-attachments/assets/cc8c9244-d263-469c-abfd-8ba876c793cb)

5. Database
    before deposit money
   
    ![Screenshot 2024-12-13 205954](https://github.com/user-attachments/assets/427c2daa-bba0-45f0-be69-77199de98b3d)

   after deposit money

   ![Screenshot 2024-12-13 210030](https://github.com/user-attachments/assets/37fb30b5-2166-40ab-a2ff-ff45a6920bbb)

## Contributing
Feel free to fork this repository and submit pull requests. Any suggestions or improvements are welcome!
   


## License
This project is open-source and available under the MIT License.

  
### Steps to Add Screenshots:

1. **Take Screenshots**:
 
   - Run your banking system and take screenshots of the various screens (Home Screen, Account Creation, Account Details, Deposit, and Withdraw screens).

3. **Upload Screenshots**:
 
   - Create a folder named `images` (or any other name of your choice) in your GitHub repository.
   - Upload the screenshots into this folder. 
   - Ensure that the screenshot file names are the same as referenced in the `README.md` (e.g., `screenshot_home.png`, `screenshot_new_account.png`, etc.).

5. **Update Paths in `README.md`**:
 
   - The `README.md` file already includes placeholders for the screenshots. Ensure that the paths to the screenshots are correct (e.g., `images/screenshot_home.png`).

7. **Commit and Push**:
 
   - Commit the `README.md` file along with the images to your GitHub repository.










   

