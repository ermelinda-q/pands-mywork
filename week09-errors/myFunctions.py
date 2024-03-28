# Programming and Scripting - Week 9
# Module of useful functions
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani
import logging 
logging.basicConfig(filename="./bank.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-(lineno)d")

# prog does stuff
balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the amount ({amount}) should never be less than 0")
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.critical(f"trying to withdraw more ({amount}) than is in the account ({balance})")
        raise ValueError("not enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount} new balance is {balance}")
    return balance

if __name__ == "__main__":
    assert withdraw(20) == 80, "incorrect calculations"
    try:
        withdraw(-1)
        assert False, "should have thrown a value error"
    except ValueError as ve:
        pass
    
    try:
        withdraw(110)
        assert False, "can't withdraww more than is in balance"
    except ValueError as ve:
        pass
    print("all good")