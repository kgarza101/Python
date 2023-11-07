
class Account:
    def __int__(self, account, password, balance = 0, transactions = [list()]):
        self.account = input("Enter your account: ") 
        self.password = input("Enter your password: ") 
        self.balance = 0
        self.transactions = [list()]


    def deposit(self):
        amount = int(input("Ammount to deposit: "))
        self.balance += amount
        print(f"Amount deposited: {amount}")
    
    
    def withdraw(self):
        amount = int(input("Ammount to withdrawl: "))
        self.balance -= amount
        print(f"Amount withdrawled: {amount}")
    
    
    def display(self):
        print(f"Current balance: {self.balance}")
    
    def history(self):
        print("")
        pass