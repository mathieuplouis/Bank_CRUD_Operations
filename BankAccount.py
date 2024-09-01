class BankAccount:
    def __init__(self, account_id, account_holder_name, account_balance):
        self.account_id = account_id
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance


    def __str__(self):
        return f"Account ID: {self.account_id}, Holder: {self.account_holder_name}, Balance: ${self.account_balance:.2f}"