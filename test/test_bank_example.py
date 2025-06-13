import pytest

# Import the implementation under test instead of redefining it here
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bank_example import BankAccount


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
