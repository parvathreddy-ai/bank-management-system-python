class Bank:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    def deposit(self):
        a=int(input("enter the amount you want to deposit:"))
        self.amount=a+self.amount
        print(f"amount deposited\nThank you {self.name} Visit again")
    def withdraw(self):
        a=int(input("enter the amount you want to withdraw:"))
        if a>self.amount:
            print("you dont have sufficient balance")
        else:
            self.amount=self.amount-a
            print(f"amount withdrawed\nThank you {self.name} Visit again")
    def check_balance(self):
        print(f"your current balnce is {self.amount}")
b1=Bank("bablu",10000)
print("welcome to abc bank")
while True:
    print("what you want to do:\n1)Deposit\n2)Withdrawl\n3)Check Balance\n4)Exit")
    a=int(input())
    if a==1:
        b1.deposit()
    elif a==2:
        b1.withdraw()
    elif a==3:
        b1.check_balance()    
    elif a==4:
        print("thankyou for visiting abc banks")
        break  
    else:
        print("please selct a valid response")
        
