class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance


    def set_account_number(self, value):
        self.account_number = value

    def set_balance(self, value):
        self.balance = value

    def withdraw(self, value):
        if value>self.balance:
            print("Cannot overdraw!")
            return 0
        else:
            balance -= value
        return value
    
    def deposit(self, value):
        balance += value
    
