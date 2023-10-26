# BANKING SYSTEM APPLICATION

#### Description: This project provides a simple Bank Account Management System where users can create and manage their bank accounts. It uses a `tkinter` based GUI for interaction and pickle for data persistence.

## Features:

- **GUI Interface**: User-friendly graphical interface for all banking operations.
- **Account Management**: Create, view, and delete accounts.
- **Transaction Operations**: Deposit, withdraw, and transfer funds between accounts.
- **Transaction History**: View detailed transaction history for each account.
- **Search Functionality**: Search for accounts by name.

## Prerequisites:

- Python 3.x
- Dependencies from `requirements.txt`

## Setup:

1. Clone this repository: git clone https://github.com/nevzatsevinc/harvard_cs50p_problem_sets_and_final_project.git
2. Navigate to the project directory: cd /final_project
3. Install the required dependencies: pip install -r requirements.txt

## Usage:
Start the application: python project.py

## Testing:
To run the tests: pytest test_project.py

## Tutorial:

Welcome to the Banking System Application tutorial! This GUI-based application allows users to perform various banking operations, such as creating accounts, depositing and withdrawing money, viewing transaction history, and more.

1. Creating a New Account
    * Click on the "Create Account" button.
    * Enter the desired account number and name.
    * Click "OK" to create the account.
2. Depositing Money
    * Click on the "Deposit" button.
    * Enter the account number.
    * Enter the amount you wish to deposit.
    * Click "OK". You'll receive a confirmation message.
3. Withdrawing Money
    * Click on the "Withdraw" button.
    * Enter the account number.
    * Enter the amount you wish to withdraw. (Ensure sufficient balance)
    * Click "OK". You'll receive a confirmation message.
4. Viewing Account Balance
    * Click on the "Check Balance" button.
    * Enter the account number for which you'd like to view the balance.
    * Click "OK". A window will display the current balance for the specified account.
5. Transferring Money
    * Click on the "Transfer Money" button.
    * Enter the source account number.
    * Enter the target account number.
    * Enter the amount you wish to transfer.
    * Click "OK". You'll receive a confirmation message.
6. Viewing Transaction History
    * Click on the "View Transaction History" button.
    * Enter the account number.
    * Click "OK". A window will display the transaction history for the specified account.
7. Searching Accounts
    * Click on the "Search Account by Name" button.
    * Enter the name or part of the name to search for.
    * Click "OK". A list of matching accounts will be displayed.
8. Viewing All Accounts
    * Click on the "Show All Accounts" button to view a list of all created accounts.
9. Deleting an Account
    * Click on the "Delete Account" button.
    * Enter the account number you wish to delete.
    * Click "OK". You'll receive a confirmation message.
10. Exiting the Application
    * Click on the "Exit" button to close the application.

## The requirements.txt file lists the dependencies for the project:

    Dependencies for project.py:
    pickle: For serializing and deserializing Python objects.
    tkinter: A standard GUI library for Python.
    datetime: To handle dates and times.

    Dependencies for test_project.py:
    pytest: A framework used for testing Python code.

## The test_project.py script is designed to test the functionality of the banking system application. Here's a brief summary:

    Fixtures:
    bank_system(): Sets up a fresh bank system instance.
    account(): Sets up a sample bank account.
    populated_bank_system(): Creates a bank system already containing an account.

    Tests:
    test_create_account(): Ensures that account creation works correctly.
    test_create_duplicate_account(): Verifies that duplicate accounts can't be created.
    test_deposit(): Tests the deposit functionality.
    test_withdraw(): Checks if the withdrawal of funds works correctly.
    test_withdraw_insufficient_funds(): Tests withdrawal with insufficient funds.
    test_transfer(): Tests fund transfer between two accounts.
    test_transfer_insufficient_funds(): Checks the fund transfer with insufficient funds in the source account.
    test_delete_account(): Verifies the account deletion functionality.
    test_delete_nonexistent_account(): Checks the scenario when trying to delete a non-existent account.
    
## Classes & Methods:

### 1. BankAccount: 
    Represents individual bank accounts with functionalities like:
    deposit(): Deposits money into the account.
    withdraw(): Withdraws money from the account.
    get_balance(): Returns the current balance.
    show_transaction_history(): Shows the transaction history.
    transfer(): Transfers money from one account to another.

### 2. BankSystem: 
    Represents the banking system with functionalities like:
    create_account(): Creates a new account.
    delete_account(): Deletes an existing account.
    search_accounts_by_name(): Searches for accounts by name.
    
### 3. BankApp: 
    The main GUI for the application built using tkinter which provides functionalities such as deposit, withdrawal, transfers, transaction history display, search, and more.
