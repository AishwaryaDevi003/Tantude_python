g=9
print("Glass Bottel cost is", g)
p=7
print("Plastic Bottel cost is", p)
glass_r=5
print("Glass Bottle return price is", glass_r)
available=int(input("Enter the amount of money you have: "))
glass=int(input("Enter the num of glass bottle: "))
pastic=int(input("Enter the num of plastic bottle: "))

for i in range(glass):
    if available >= g:
        available -= g
        available += glass_r
        print("Glass bottle purchased")
    else:
        print("Not enough money for glass bottle")
        break
for i in range(pastic):
    if available >= p:
        available -= p
        print("Plastic bottle purchased")
    else:
        print("Not enough money for plastic bottle")
        break

    
    