class cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        result = self.a + self.b
        print("The result of addition is", result)
    def subtract(self):
        result = self.a - self.b
        print("The result of subtraction is", result)
    def multiply(self):
        result = self.a * self.b
        print("The result of multiplication is", result)
    def divide(self):
        if self.b == 0:
            print("Cannot divide by zero")
        else:
            result = self.a / self.b
            print("The result of division is", result)
    def exit(self):
        print("Exiting the calculator. Thank you for using our service!")



print("enter the option\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
option = int(input("Enter your option: "))
print ("enter two number")
a=int(input())
b=int(input())
o=cal(a,b)
if option == 1:
    o.add()
elif option == 2:
    o.subtract()
elif option == 3:
    o.multiply()
elif option == 4:
    o.divide()
else:
    o.exit()
    
    
    
    
