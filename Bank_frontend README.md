# Banking System with Tkinter and MySQL

A simple banking system created using Python's Tkinter for GUI and MySQL for database storage. This application allows users to create accounts, log in, deposit, withdraw, and check account details.

## Features:
- **Login**: Users can log in with their name and pin.
- **Create Account**: Users can create a new account by providing personal details.
- **View Account Details**: Once logged in, users can view their personal information, balance, and total balance.
- **Deposit and Withdraw**: Users can deposit or withdraw money from their account.
- **Responsive Fullscreen**: The application is designed to run in fullscreen mode for a better user experience.

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
  

  ![Screenshot 2024-12-13 212552](https://github.com/user-attachments/assets/b2bc2148-95fe-4aae-bcac-2b7c0eb838be)


  ### Deposit Screen:
  

  ![Screenshot 2024-12-13 212615](https://github.com/user-attachments/assets/1639b7dc-205e-447d-9b08-b979f3778a60)



  ### Withdraw Screen:
  

  ![Screenshot 2024-12-13 212631](https://github.com/user-attachments/assets/585d1345-4b70-465a-92cb-e89722f9205e)



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





