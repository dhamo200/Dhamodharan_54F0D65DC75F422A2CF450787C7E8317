class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("123456789", "John Doe", 1000.0)

    # Test deposit and display_balance
    my_account.display_balance()
    my_account.deposit(500.0)
    my_account.display_balance()

    # Test withdrawal and display_balance
    my_account.withdraw(200.0)
    my_account.display_balance()
    my_account.withdraw(1500.0)  # This should result in an error message