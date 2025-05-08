from bank_account import BankAccount

account_1 = BankAccount(12345, 9999, "hello! :3")
account_2 = BankAccount(10987, 3939, "Miekyu")

print("Account num:", account_1.get_account_number(), "\nBalance:", account_1.get_balance())

account_1.set_account_number(account_1.get_account_number() + 20)
account_1.set_balance(200003)

print("Account num:", account_1.get_account_number(), "\nBalance:", account_1.get_balance(), "\n\n\n\n")


print("Account num:", account_2.get_account_number(), "\nBalance:", account_2.get_balance())

account_2.set_account_number(account_2.get_account_number() - 20)
account_2.set_balance(39393939)

print("Account num:", account_2.get_account_number(), "\nBalance:", account_2.get_balance())




account_2.deposit(account_1.withdraw(50000000000))
account_2.deposit(account_1.withdraw(2000))

account_1.deposit(account_2.withdraw(50000000000))
account_1.deposit(account_2.withdraw(2000))