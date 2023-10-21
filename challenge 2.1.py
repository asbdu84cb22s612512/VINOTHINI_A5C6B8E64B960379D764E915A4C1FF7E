#Implement a class called Bank Account that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the Bank Account class and test the deposit and withdrawal functionality.


class BankAccount:

  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance


def deposit(self, amount):
  if amount > 0:
    self.__account_balance += amount
    return f"Deposited ₹{amount}. Newbalance: ₹{self.__account_balance}"
  else:
    return "Invalid deposit amount. please deposit a positive amount."


def withdraw(self, amount):
  if 0 < amount <= self.__account_balance:
    self.__account_balance -= amount
    return f"withdraw ₹{amount}. New balance: ₹{self.__amount_balance}"
  else:
    return "Invalid withdrawal amount or insufficient balance."


def display_balance(self):
  return f"Account balance for {self._account_holder_name}: ₹{self._account_balance}"
