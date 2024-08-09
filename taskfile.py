#1
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "File not found."

file_path = 'test.txt'
word_count = count_words_in_file(file_path)
print(f"The number of words in the file is: {word_count}")

#2
def write_names(file_path, names):
    with open(file_path, 'w') as file:
        for name in names:
            file.write(name + '\n')

names = ["Sree", "Manu", "Charlie", "Dia"]
file_path = 'names.txt'
write_names(file_path, names)
print(f"Names have been written to {file_path}.")

#3
squares_of_even = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_of_even)

#
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"The current balance is {self.balance}.")
        return self.balance
    # Creating a new bank account
account = BankAccount("John Doe", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

