
class Bank:
    def __init__(self,account_no,balance):
        self.accountNo = account_no
        self.balance = balance
    def debit(self,amount):
        self.balance-=amount
    
    def credit(self,amount):
        self.balance+=amount
    
    def balance(self):
        return self.balance
    

b1 = Bank(1,5000)
b1.credit(4000)
b1.debit(2500)
print(b1.balance)