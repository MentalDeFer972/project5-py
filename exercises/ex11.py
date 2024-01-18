# Write your code here


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try:
            if self.balance < amount or self.balance < 0:
                raise Exception("Moyens insuffisants.")
            else:
                self.balance -= amount
        except Exception as e:
            print(e)

    def display_balance(self):
        print(
            f"Nom du propiétaire : {self.account_holder}, \nSolde:                    {self.balance}"
        )


ba = BankAccount("Joffrey", 560.38)

ba.deposit(100)

ba.display_balance()

ba.deposit(-100)

ba.display_balance()

ba.withdraw(561.38)

ba.display_balance()
