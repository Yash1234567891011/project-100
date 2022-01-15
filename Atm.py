class ATM:
    def __init__(self, name, account_number, pin_number):
        self.name = name
        self.account_number = account_number
        self.pin_number=pin_number
        self.balance=50000
         
    def account_detail(self):
        print("----------ACCOUNT DETAIL----------")
        print("Account Holder:",{self.name})
        print("Account Number:", {self.account_number})
        print("Account pin: ",{self.pin_number})
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
       
    def Withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        print("Current account balance: Nu.", self.balance)
def main():
    name=input("Enter your name:")
    acc_number=int(input("Enter your account number:"))
    pin_number=int(input("Enter your pin number:"))
    user=ATM(name,acc_number,pin_number)
    print("Choose your activity")
    print("1.Account detial 2.Withdrawal 3.Deposite")
    activity=int(input("Enter activity number:"))
    if(activity==1):
        user.account_detail()
    elif(activity==2):
        amount=int(input("Enter your amount:"))
        user.Withdrawal(amount)  
    elif(activity==3):
        amount=int(input("Enter your amount:"))
        user.deposit(amount) 
    else:
        print("Enter your vaild number") 
if __name__=="__main__":
    main()                