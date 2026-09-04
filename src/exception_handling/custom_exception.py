class InsufficientBalanceError(Exception):
    pass

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )
        self.balance -= amount

account = BankAccount(5000)
try:
    account.withdraw(10000)
except InsufficientBalanceError as error:
    print(error)