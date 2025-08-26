#bank account program

class bank_account:
    def __init__(self,account_number,owner,balance=0):
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
    
    def check_balance(self):
        print(f"the balance in your account is:{self.balance}")

    def amt_deposit(self,deposit):
        if deposit >0:
            self.balance+=deposit
            print(f"amount deposited is:₹{deposit}.  new balance is:₹{self.balance}")
        else:
            print("enter the valid value to deposit")

    def amt_withdraw(self,withdraw):
        if withdraw > self.balance:
            print(f"your account balance is:₹{self.balance} amount entered for withdraw is:₹{withdraw}")
        else:
            self.balance -=withdraw
            print(f"entered amount for withdraw is:₹{withdraw}. new balance is:₹{self.balance}")

    def details(self):
        print(f"the name of the owner is:{self.owner} and {self.owner} bank account number is:{self.account_number}")
        


#user inputs the details 
account_num=str(input("enter the account number:"))
name=str(input("enter your name:"))
depo=int(input("enter the amount to be deposited:"))
withdrw=int(input("enter the amount you want to withdraw:"))
print()

#assigning value to class
user1_account=bank_account(account_num,name,500)

#printing details
user1_account.amt_deposit(depo)
user1_account.check_balance()
user1_account.amt_withdraw(withdrw)
user1_account.details()