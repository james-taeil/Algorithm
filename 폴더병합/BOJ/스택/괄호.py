blist = []

T = int(input())

for i in range(T):
    PS = list(input())
    sum = 0
    for i in PS:
        if i == "(":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")