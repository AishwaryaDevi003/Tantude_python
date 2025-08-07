num=int(input())
n=len(str(num))
t=num
sum=0

while t>0:
    d=t%10
    sum+=d**n
    t=t//10
if sum==num:
    print("Amstrong")
else:
    print("Not an amstrong")
    
    