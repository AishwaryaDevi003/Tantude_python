def ins(a):
    for i in range(1,len(a)):
        while i>0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
a=list(map(int,input().split()))
ins(a)
print(a)

            