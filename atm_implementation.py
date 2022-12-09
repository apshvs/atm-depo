"""
Created on Fri Nov 18 14:32:48 2022

@author: Akshay
"""
from datetime import datetime as d
class Atm:
    def __init__(self, bal):
        self.balance = bal

    def deposit(self, dep):
        self.balance += dep
        file.write("Deposit of:"+str(dep)+" at "+str(d.now())+"\n")

    def withdraw(self, withd):
        if withd > self.balance:
            print("Insufficient Balance",self.balance)
            file.write("Withdrawal Declined Due to Insufficient Balance"+"\n")
        else:
            self.balance -= withd
            file.write("Withdrawal of:"+str(withd)+" at "+str(d.now())+"\n")

    def check_balance(self):
        if self.balance<5000:
            print("LOW BALANCE>>>>>>>>>>",end=" ")
        file.write("Balance is:"+str(self.balance)+" at "+str(d.now())+"\n")
        return(self.balance)

user_name=input("Enter Your Name:")
user_name=user_name.capitalize()
print("Welcome",user_name)
user = Atm(5000)
file = open('log.txt','w')
file.write("Name:"+str(user_name)+"\n")
choice = input("1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit\nPlease enter your choice:")

while choice in ["1","2","3","4"]:
    if choice == '1' :
        de = int(input("enter the amount to deposit: "))
        user.deposit(de)
        print("Available Balance:",end=" ")
        print(user.check_balance())

    elif choice == '2':
        wi = int(input("enter the amount to withdraw: "))
        user.withdraw(wi)
        print("Available Balance:",end=" ")
        print(user.check_balance())

    elif choice == "3":
        print("Name:",user_name)
        print("Account Type: Savings")
        print("Balance in your saving account is:",end="")
        print(user.check_balance())
        trxn=input("Do You Want To View Transction History?[Y/N]")
        if trxn in ["y","Y"]:
            file.close()
            file = open("log.txt", "r")
            print (file.read())
            file.close()
        file = open('log.txt','a')
    elif choice=="4":
        print("THANK YOU FOR USING OUR SERVICES!!!")
        file.close()
        break
    

    while True:
        stop=input("Return to Main Menu[Y/N]:")
        if stop in ["y","Y"]:
            choice = input("1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit\nPlease enter your choice:")
            break
        elif stop in ["n","N"]:
                file.close()
                print("THANK YOU FOR USING OUR SERVICES!!!")
                choice=0
                break
        else:
            print("Please Enter Valid Input!!!!")
        
                
                
