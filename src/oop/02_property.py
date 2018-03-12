#!/usr/bin/env python

class Account(object):
    """The Account class,
    The amount is in dollars.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        "The amount of money in the account"
        "Amazing world"
        return self.__amt

    @property
    def inr(self):
        "Gives the money in INR value."
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=61) # Based on today's value of INR :(
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In INR:", acc.inr)
    acc.amount = -100
    print("Dollar amount:", acc.amount)
    print(__doc__)
    print(__package__)
    print(__spec__)
    print("Name : ",__name__)
    print("File :",__file__)         #Provides the complete path for current file
    print(acc.rate)
    print(acc.inr)
    