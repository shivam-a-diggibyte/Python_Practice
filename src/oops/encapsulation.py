class BankAccount:
    def __init__(self, balance):
        self._balance = balance      # "protected" by convention

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())
