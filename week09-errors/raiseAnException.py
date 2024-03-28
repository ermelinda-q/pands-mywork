# Programming and Scripting - Week 9
# This program prompts the user for an amount and withdraws it from an account
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")
    balance = balance - amount
    return balance

amount = int(input("amount to withdraw:"))

print(withdraw(amount))