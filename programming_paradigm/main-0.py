import sys
from bank_account import BankAccount
def main():
    # Create a BankAccount object (starting with $0)
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> : [amount]")
        print("Available operations: deposit, withdraw, display_balance")
        sys.exit(1)

    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) < 3:
            print("Please specify the amount to deposit.")
            sys.exit(1)
        amount = float(sys.argv[2])
        account.deposit(amount)
        account.display_balance()

    elif operation == "withdraw":
        if len(sys.argv) < 3:
            print("Please specify the amount to withdraw.")
            sys.exit(1)
        amount = float(sys.argv[2])
        success = account.withdraw(amount)
        if success:
            account.display_balance()
        else:
            print("Insufficient funds.")

    elif operation == "balance":
        account.display_balance()
    else:
        print(f"Unknown operation: {operation}")
        print("Available operations: deposit, withdraw, balance")
if __name__ == "__main__":

    main()