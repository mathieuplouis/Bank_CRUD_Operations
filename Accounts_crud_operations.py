import BankAccount as bankaccount
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, account_holder, initial_balance):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists.")
        self.accounts[account_id] = bankaccount.BankAccount(account_id, account_holder, initial_balance)
        print(f"Account created: {self.accounts[account_id]}")

    def read_account(self, account_id):
        account = self.accounts.get(account_id)
        if account:
            return account
        else:
            raise ValueError("Account not found.")

    def update_account(self, account_id, new_account_holder=None, new_balance=None):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found.")
        if new_account_holder:
            account.account_holder = new_account_holder
        if new_balance is not None:
            if new_balance < 0:
                raise ValueError("Balance cannot be negative.")
            account.balance = new_balance
        print(f"Account updated: {account}")

    def delete_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print(f"Account with ID {account_id} deleted.")
        else:
            raise ValueError("Account not found.")

def main():
    bank = Bank()

    # Create some accounts
    try:
        bank.create_account("12345", "Alice", 1000)
        bank.create_account("67890", "Bob", 500)
    except ValueError as e:
        print(e)

    # Read an account
    try:
        account = bank.read_account("12345")
        print(f"Read account: {account}")
    except ValueError as e:
        print(e)

    # Update an account
    try:
        bank.update_account("12345", new_account_holder="Alicia", new_balance=1200)
    except ValueError as e:
        print(e)

    # Delete an account
    try:
        bank.delete_account("67890")
    except ValueError as e:
        print(e)

    # Attempt to read a deleted account
    try:
        bank.read_account("67890")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
