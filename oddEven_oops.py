class oddreven:
    def __init__(self,num):
        self.num = num
    def odd_even(self):
        for i in range(len(self.num)):
            if self.num[i] % 2 ==0:
                print(self.num[i],"even")
            else:
                print(self.num[i],"odd")



num=list(map(int,input("Enter a number: ").split()))
o=oddreven(num)
o.odd_even()
