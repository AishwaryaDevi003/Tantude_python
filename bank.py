available_balance=10
n=list(map(int,input().split()))
t=len(n)
for i in range(t):
    if n[i] <= available_balance:
        available_balance -= n[i]
        print(1)
    else:
        print(0)
