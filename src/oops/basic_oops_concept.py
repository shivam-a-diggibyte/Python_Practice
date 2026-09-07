class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Current balance: ₹{self.balance}")


account = BankAccount("Shivam", 10000)

account.show_balance()

account.deposit(5000)

account.withdraw(3000)

account.show_balance()