class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit(self.balance)

    def commit(self, amount):
        with open(self.filepath, 'w') as file:
            file.write(str(amount))

account = Account("account//balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(200)
print(account.balance)
