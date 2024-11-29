class BankExpection(Exception):
    pass

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

    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BankExpection(
                f"\nSorry,account {self.name} only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete.")
            self.get_Balance()
        except BankExpection as error:
            print(f"\nWithdraw interrupted:{error}")
        