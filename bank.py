# ------------------------------BANK ACCOUNT QUESTION----------------------------
class Account():

    # initilazing bank account with balance,account_no as its parameter.
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    # debit method
    def debit(self,amouunt):
        self.balance-=amouunt
        print (f"Rs. {amouunt} was debited from account number {self.account_no}.")
        print(f"Remaining Balance : {self.get_balance()}\n")


    # credit method
    def credit(self,amouunt):
        self.balance+=amouunt
        print (f"Rs. {amouunt} was credited in account number {self.account_no}.")
        print(f"Remaining Balance : {self.get_balance()}\n")

    def get_balance(self):
        return self.balance

acc1=Account(10000,123456789)
acc2=Account(2000,1234)


acc1.debit(1000)
acc2.credit(40000)
acc1.credit(200)
