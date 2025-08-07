num=int(input())
a=""
num_s=str(num)
for i in range(len(num_s)-1,-1,-1):
    a+=num_s[i]
print(a)