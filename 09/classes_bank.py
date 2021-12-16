class Bank_account():
    def __init__(self,number):
        self.number = number
        self.balance = 0

    def display(self):
        print(
f"""Bank account No: {self.number}
Balance: {self.balance} PLN
""")

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds on the account\n")

bank = Bank_account("12 3456 5555 9090 1111 0000 7722")
bank.display()
bank.deposit(25.30)
bank.display()
bank.withdraw(31.70)
bank.display()
bank.withdraw(14)
bank.display()