arr = []

for i in input():
    arr.append(int(i))
    
arr.sort(reverse=True)

for a in arr:
    print(a, end="")