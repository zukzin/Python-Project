# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = 10 #changed default behaviour

    def spend_cash(self, amount):
        if self.balance < amount:
            pass # removed exception
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount - 20 #trying to break the test

