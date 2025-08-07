class atm:
    def __init__(self, name, initial_amount):
        self.name = name
        self.balance = initial_amount
    def deposit(self):
        self.balance=amount+self.balance
        print("Your new balance is", self.balance)
    def withdraw(self):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Your new balance is", self.balance)





name=input("Enter your name: ")
initial_amount=float(input("Enter initial amount: "))
o=atm(name,initial_amount)
print("enter an option\n1.Deposit\n2.withdraw\n3.exit")
option=int(input("Enter your option: "))
if option ==1:
    amount=float(input("Enter amount to deposit: "))
    o.deposit()
elif option ==2:
    amount=float(input("Enter amount to withdraw: "))
    o.withdraw()
else:
    print("Exiting the ATM. Thank you for using our service!")
