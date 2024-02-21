# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.balance = bal

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount):
        self.balance += abs(amount)

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient Funds")
        else:
          self.balance -= abs(amount)
        

      # The get_balance method returns the
      # account balance.

    def get_balance(self):
        return self.balance



    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
