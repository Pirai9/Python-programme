class BankAccount:
    def __init__(self,initial_amount,acct_name):
        self.balance=initial_amount
        self.name=acct_name
        print(f"\nAccount'{self.name}'created.\nBalance=${self.balance:.2f}")
    
    def get_Balance(self):
        print(f"\nAccount'{self.name}'\nBalance=${self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("\nDeposit Complet.")
        self.get_Balance()