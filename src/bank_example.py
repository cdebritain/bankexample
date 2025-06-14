class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount")

    def display_balance(self):
        print(f"{self.owner}'s account balance: ₹{self.balance}")


if __name__ == "__main__":
    # Example usage
    account1 = BankAccount("Isha", 1000)

    account1.display_balance()
    account1.deposit(500)
    account1.withdraw(300)
    # This should trigger "Insufficient funds or invalid amount"
    account1.withdraw(1500)
