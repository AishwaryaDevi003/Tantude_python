n=list(map(int,input().split()))
l=n[0]
for i in range (1,len(n)):
    if n[i]>l:
        l=n[i]
print(l)
