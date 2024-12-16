# Banking System with Tkinter and MySQL

A simple banking system created using Python's Tkinter for GUI and MySQL for database storage. This application allows users to create accounts, log in, deposit, withdraw, and check account details.

## Features

### 1. **Login Screen**
   - Users can log in using their name and PIN.
   - Upon successful login, users are redirected to their account details page.
   - If the login credentials are incorrect, an error message is displayed.

### 2. **Account Creation**
   - Users can create a new account by providing the following details:
     - Name
     - Gender
     - Age
     - City
     - State
     - PIN
   - A unique 11-digit account number is generated for each new account.
   - The account information is stored in the MySQL database.

### 3. **Account Details**
   - After logging in, users can view their account details, including:
     - Name
     - Gender
     - Age
     - City
     - State
     - Balance
     - Total Balance
   - Users can perform the following operations:
     - **Deposit**: Users can add funds to their account.
     - **Withdraw**: Users can withdraw funds if sufficient balance is available.
     - **Delete Account**: Users can delete their account permanently.

### 4. **Transaction Handling**
   - **Deposit**: Allows users to deposit money into their account, updating both the balance and total balance.
   - **Withdraw**: Allows users to withdraw money from their account, with a check to ensure sufficient balance.

### 5. **Account Deletion**
   - Users can delete their account by confirming their action. Once deleted, the account information is removed from the database.

### 6. **MySQL Database Integration**
   - The application uses MySQL to store user data securely.
   - The `details` table contains fields like `name`, `gender`, `age`, `city`, `state`, `pin`, `account_number`, `balance`, and `total_balance`.

### 7. **User Interface**
   - The GUI is built with `tkinter` and offers a full-screen window.
   - The application has a blue color scheme for a visually clean experience.

## Requirements:
1. **Python 3.x**: You need Python 3 or higher to run this application.
2. **Tkinter**: This is used for the graphical user interface (GUI).
3. **MySQL**: A MySQL database to store user data.

## Prerequisites:
- Install Python 3.x (https://www.python.org/)
- Install MySQL Server (https://dev.mysql.com/downloads/installer/)

### Install Required Libraries:

```bash
  pip install mysql-connector-python
```

## Setup the MySQL Database:
Before running the application, make sure you have a MySQL database set up. You can create the bank_users database and the details table using the following SQL commands:


CREATE DATABASE bank_users;

  
    USE bank_users;
  

    CREATE TABLE details 
    (
  
    name VARCHAR(50),
    
    gender VARCHAR(20),
    
    age INT,
    
    city VARCHAR(50),
    
    state VARCHAR(50),
    
    pin INT,
    
    account_number BIGINT PRIMARY KEY,
    
    balance BIGINT,
    
    
    total_balance BIGINT
   
    );


## How to Run:
1. Clone this repository to your local machine.
2. Open a terminal/command prompt in the project directory.
3. Run the application with the following command.
 ```bash
 python bank_system.py
```
## Screenshots:
  Here are some screenshots of the application:
  
  ### Login Screen:
  
  ![Screenshot 2024-12-13 212309](https://github.com/user-attachments/assets/3f017eed-a61c-4e49-a875-eda8f21c4fdb)


  ### Create Account Screen:
  
  
  ![Screenshot 2024-12-13 212350](https://github.com/user-attachments/assets/6e7502e8-ef32-49ea-91af-a35afb1a490b)


  ### Account Details Screen:
  

  ![Screenshot 2024-12-16 171644](https://github.com/user-attachments/assets/b6f97790-a815-441a-9b44-f4cc08e95177)



  ### Deposit Screen:
  

  ![Screenshot 2024-12-13 212615](https://github.com/user-attachments/assets/1639b7dc-205e-447d-9b08-b979f3778a60)


  


  ![Screenshot 2024-12-16 171657](https://github.com/user-attachments/assets/3393390e-fa8e-48d8-af4d-cd0a9b089a44)




  ### Withdraw Screen:
  

  ![Screenshot 2024-12-13 212631](https://github.com/user-attachments/assets/585d1345-4b70-465a-92cb-e89722f9205e)




  ![Screenshot 2024-12-16 171712](https://github.com/user-attachments/assets/82806bdf-596a-4316-b764-7e08decd74d8)




## Contributing:
 - If you want to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or bug fixes.

## License:
-This project is open-source and available under the MIT License.


## Author:
Piyush ghavari


### How to Use:
- Replace the `"images/screenshot_login.png"` and similar paths with the actual paths of your screenshots.
- Add any specific instructions about the app, such as setting up your database, depending on your environment.

This `README.md` provides a brief description of your project, its features, installation requirements, setup instructions, and screenshots. It will make your repository more informative for others who may want to use or contribute to the project.





