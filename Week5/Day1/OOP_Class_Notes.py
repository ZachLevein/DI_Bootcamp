
class Shark():
    def __init__(self, name, size):
        self.name = name
        self.size = size #attributes
    
# Creating a method
    def bite(self):
        print('Attack, you have been bitten')
        return 'done'
#Insatntiating a new Shark object
shark1 = Shark('GreatWhite', 6)

print(shark1)

#calling on the method
print(shark1.bite())

#To see the full blueprint of the object 
help(shark1)


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.history = []
    def view_balance(self):
        self.history.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.history.append(f"Deposit: {amount}")
            print("Deposit Succcessful")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.history.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount
    def view_history(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.history:
            print(transaction)
# account = BankAccount('5675309')
# print(account.balance)