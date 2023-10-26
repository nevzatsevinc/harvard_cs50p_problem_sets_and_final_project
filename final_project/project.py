"""
My Final Project - BANKING SYSTEM APPLICATION
Description: This project provides a simple Bank Account Management 
System where users can create and manage their bank accounts. 
It uses a `tkinter` based GUI for interaction and pickle for data persistence.
https://cs50.harvard.edu/python/2022/project/

https://github.com/nevzatsevinc/harvard_cs50p_problem_sets_and_final_project
"""


import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
from datetime import datetime


# BankAccount Class: Represents individual bank accounts.
class BankAccount:

    # Constructor: Initializes an account with an account number, name, and initial balance.
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = 0.0  # Start with a zero balance
        self.transactions = []  # List to store transaction history

    def _current_datetime_str(self):
        """Get the current date and time as a string."""
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Deposit money into the account and record the transaction.
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"{self._current_datetime_str()} - Withdrew {amount}")
        return f"{amount} deposited to account {self.account_number}!"

    # Withdraw money from the account and record the transaction.
    # Check if enough balance is available.
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        self.transactions.append(f"{self._current_datetime_str()} - Withdrew {amount}")
        return f"{amount} withdrawn from account {self.account_number}!"

    # Return the current balance of the account.
    def get_balance(self):
        return f"Account balance: {self.balance}"
    
    # Return the transaction history as a string.
    def show_transaction_history(self):
        return "\n".join(self.transactions)

    # Transfer money from this account to another account.
    # Record the transaction in both accounts.
    def transfer(self, target_account, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(f"{self._current_datetime_str()} - Transferred {amount} to {target_account.account_number}")
        target_account.transactions.append(f"{self._current_datetime_str()} - Received {amount} from {self.account_number}")
        return f"{amount} transferred from {self.account_number} to {target_account.account_number}!"


# BankSystem Class: Manages a collection of bank accounts.
class BankSystem:

    # Constructor: Load accounts from file or start with an empty collection.
    def __init__(self):
        self.accounts = self.load_accounts()

    # Save accounts to a file for data persistence.
    def save_accounts(self):
        with open("accounts.pkl", "wb") as file:
            pickle.dump(self.accounts, file)

    # Load accounts from a file. If the file doesn't exist, return an empty dictionary.
    @staticmethod
    def load_accounts():
        try:
            with open("accounts.pkl", "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return {}

    # Create a new bank account and save it.
    def create_account(self, account_number, account_name):
        if account_number in self.accounts:
            return "Account already exists!"
        self.accounts[account_number] = BankAccount(account_number, account_name)
        self.save_accounts()
        return f"Account created for {account_name} with account number {account_number}!"

    # Delete a bank account and update the saved file.
    def delete_account(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist!"
        del self.accounts[account_number]
        self.save_accounts()
        return f"Account {account_number} deleted successfully!"
    
    # Search for accounts by name.
    def search_accounts_by_name(self, name_query):
        matching_accounts = {acc_num: acc for acc_num, acc in self.accounts.items() if name_query.lower() in acc.account_name.lower()}
        return matching_accounts


# BankApp Class: GUI interface for the bank system.
class BankApp:

    # Constructor: Set up the main window and add buttons for each action.
    def __init__(self, root, bank_system):
        self.root = root
        self.bank_system = bank_system
        self.root.title("Bank Account Management System")

        # Define menu items and their corresponding actions.
        self.menu = {
            "1": ("Create Account", self.create_account),
            "2": ("Deposit", self.deposit),
            "3": ("Withdraw", self.withdraw),
            "4": ("Check Balance", self.check_balance),
            "5": ("Transfer Money", self.transfer),
            "6": ("View Transaction History", self.view_transaction_history),
            "7": ("Search Account by Name", self.search_account_by_name),
            "8": ("Show All Accounts", self.show_all_accounts),
            "9": ("Delete Account", self.delete_account),
            "10": ("Exit", self.exit_app)
        }
        
        # Create and display buttons for each menu item.
        for key, (name, _) in self.menu.items():
            b = tk.Button(self.root, text=name, command=self.menu[key][1], font=("Arial", 20))
            b.pack(fill=tk.X)

    # Create a new account.
    # Prompt user for account number and name.
    def create_account(self):
        account_number = simpledialog.askstring("Input", "Enter account number:")
        account_name = simpledialog.askstring("Input", "Enter account name:")
        messagebox.showinfo("Information", self.bank_system.create_account(account_number, account_name))

    # Deposit money to an account. Prompt user for account number and deposit amount.
    def deposit(self):
        account_number = simpledialog.askstring("Input", "Enter account number:")
        if account_number not in self.bank_system.accounts:
            messagebox.showerror("Error", "Account does not exist!")
            return
        amount = float(simpledialog.askstring("Input", "Enter deposit amount:"))
        result = self.bank_system.accounts[account_number].deposit(amount)
        self.bank_system.save_accounts()
        messagebox.showinfo("Information", result)

    # Withdraw money from an account. Prompt user for account number and withdrawal amount.
    def withdraw(self):
        account_number = simpledialog.askstring("Input", "Enter account number:")
        if account_number not in self.bank_system.accounts:
            messagebox.showerror("Error", "Account does not exist!")
            return
        amount = float(simpledialog.askstring("Input", "Enter withdrawal amount:"))
        result = self.bank_system.accounts[account_number].withdraw(amount)
        self.bank_system.save_accounts()
        messagebox.showinfo("Information", result)

    # Check and display the balance of an account.
    def check_balance(self):
        account_number = simpledialog.askstring("Input", "Enter account number:")
        if account_number not in self.bank_system.accounts:
            messagebox.showerror("Error", "Account does not exist!")
            return
        result = self.bank_system.accounts[account_number].get_balance()
        messagebox.showinfo("Balance", result)

    # Transfer money between two accounts.
    def transfer(self):
        source_account_number = simpledialog.askstring("Input", "Enter source account number:")
        target_account_number = simpledialog.askstring("Input", "Enter target account number:")
        if source_account_number not in self.bank_system.accounts or target_account_number not in self.bank_system.accounts:
            messagebox.showerror("Error", "One or both account numbers do not exist!")
            return
        amount = float(simpledialog.askstring("Input", "Enter transfer amount:"))
        result = self.bank_system.accounts[source_account_number].transfer(self.bank_system.accounts[target_account_number], amount)
        self.bank_system.save_accounts()
        messagebox.showinfo("Information", result)

    # Show the transaction history of an account.
    def view_transaction_history(self):
        account_number = simpledialog.askstring("Input", "Enter account number:")
        if account_number not in self.bank_system.accounts:
            messagebox.showerror("Error", "Account does not exist!")
            return
        result = self.bank_system.accounts[account_number].show_transaction_history()
        messagebox.showinfo("Transaction History", result)

    # Search functionality
    def search_account_by_name(self):
        name_query = simpledialog.askstring("Input", "Enter name or part of name to search for:")
        matching_accounts = self.bank_system.search_accounts_by_name(name_query)
        
        if not matching_accounts:
            messagebox.showinfo("Search Result", "No matching accounts found.")
            return

        results = []
        for acc_num, acc in matching_accounts.items():
            results.append(f"Account Number: {acc_num}, Account Name: {acc.account_name}")

        result_text = "\n".join(results)
        messagebox.showinfo("Search Result", result_text)       

    # Display a list of all accounts.
    def show_all_accounts(self):
        accounts_list = []
        for acc in self.bank_system.accounts:
            accounts_list.append(f"Account Number: {acc}, Account Name: {self.bank_system.accounts[acc].account_name}")
        result = "\n".join(accounts_list)
        if not accounts_list:
            result = "No accounts available!"
        messagebox.showinfo("All Accounts", result)

    # Delete an account. Prompt user for the account number.
    def delete_account(self):
        account_number = simpledialog.askstring("Input", "Enter account number to delete:")
        result = self.bank_system.delete_account(account_number)
        messagebox.showinfo("Information", result)

    # Exit the application.
    def exit_app(self):
        self.root.quit()


# Main Execution
def main():
    # Initialize the bank system.
    bank_system = BankSystem()

    # Set up and display the GUI.
    root = tk.Tk()
    app = BankApp(root, bank_system)
    root.mainloop()  # Start the tkinter event loop.


if __name__ == '__main__':
    main()
