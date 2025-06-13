import pytest

# Original class
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


# ------------------------
# Tests
# ------------------------

@pytest.fixture
def account():
    return BankAccount("Isha", 1000)

def test_deposit_valid_amount(account, capfd):
    account.deposit(500)
    out, _ = capfd.readouterr()
    assert "₹500 deposited. New balance: ₹1500" in out
    assert account.balance == 1500

def test_deposit_invalid_amount(account, capfd):
    account.deposit(-100)
    out, _ = capfd.readouterr()
    assert "Invalid deposit amount" in out
    assert account.balance == 1000

def test_withdraw_valid_amount(account, capfd):
    account.withdraw(300)
    out, _ = capfd.readouterr()
    assert "₹300 withdrawn. New balance: ₹700" in out
    assert account.balance == 700

def test_withdraw_insufficient_funds(account, capfd):
    account.withdraw(1500)
    out, _ = capfd.readouterr()
    assert "Insufficient funds" in out
    assert account.balance == 1000

def test_display_balance(account, capfd):
    account.display_balance()
    out, _ = capfd.readouterr()
    assert "Isha's account balance: ₹1000" in out
