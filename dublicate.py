n = list(map(int, input().split()))
unique_elements = set(n)
for elem in unique_elements:
    count = n.count(elem)
    if count > 1:
        print(f"{elem} duplicated {count} times")

    
