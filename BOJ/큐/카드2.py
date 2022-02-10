n = int(input())
l = list(range(1, n + 1))

while (len(l) > 1):
    l.pop(0)
    temp = l.pop(0)
    l.append(temp)
    
print(l.pop(0))