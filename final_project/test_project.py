"""
My Final Project - BANKING SYSTEM APPLICATION
Description: This project provides a simple Bank Account Management 
System where users can create and manage their bank accounts. 
It uses a `tkinter` based GUI for interaction and pickle for data persistence.
https://cs50.harvard.edu/python/2022/project/

https://github.com/nevzatsevinc/harvard_cs50p_problem_sets_and_final_project
"""


import pytest
from project import BankSystem, BankAccount


# This fixture sets up a fresh bank system for testing purposes
@pytest.fixture
def bank_system():
    return BankSystem()

# This fixture sets up a sample bank account with a specific account number and user
@pytest.fixture
def account():
    return BankAccount("12345", "Test User")

# This fixture uses the above two fixtures to create a bank system that already contains an account
@pytest.fixture
def populated_bank_system(bank_system, account):
    bank_system.create_account("12345", "Test User")
    return bank_system

# Test to ensure creating an account works correctly
def test_create_account(bank_system):
    message = bank_system.create_account("12345", "Test User")
    assert message == "Account created for Test User with account number 12345!"
    assert "12345" in bank_system.accounts

# Test to ensure you can't create a duplicate account
def test_create_duplicate_account(populated_bank_system):
    message = populated_bank_system.create_account("12345", "Test User")
    assert message == "Account already exists!"

# Test deposit functionality for an account
def test_deposit(account):
    message = account.deposit(1000)
    assert message == "1000 deposited to account 12345!"
    assert account.balance == 1000

# Test withdrawing funds from an account
def test_withdraw(account):
    account.deposit(1000)
    message = account.withdraw(500)
    assert message == "500 withdrawn from account 12345!"
    assert account.balance == 500

# Test trying to withdraw more funds than are available
def test_withdraw_insufficient_funds(account):
    message = account.withdraw(1000)
    assert message == "Insufficient funds!"
    assert account.balance == 0

# Test transferring funds between two accounts
def test_transfer(account):
    target_account = BankAccount("67890", "Target User")
    account.deposit(1000)
    message = account.transfer(target_account, 500)
    assert message == "500 transferred from 12345 to 67890!"
    assert account.balance == 500
    assert target_account.balance == 500

# Test trying to transfer more funds than are available in the source account
def test_transfer_insufficient_funds(account):
    target_account = BankAccount("67890", "Target User")
    message = account.transfer(target_account, 1000)
    assert message == "Insufficient funds!"
    assert account.balance == 0
    assert target_account.balance == 0

# Test deleting an existing account from the bank system
def test_delete_account(populated_bank_system):
    message = populated_bank_system.delete_account("12345")
    assert message == "Account 12345 deleted successfully!"
    assert "12345" not in populated_bank_system.accounts

# Test trying to delete a non-existent account
def test_delete_nonexistent_account(bank_system):
    message = bank_system.delete_account("12345")
    assert message == "Account does not exist!"
