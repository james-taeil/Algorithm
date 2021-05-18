
def num3plue1():

    user_input = input().split()
    a = int(user_input[0])

    b = int(user_input[1])

    c = int(user_input[2])

    for i in range(len(a)):
        print(i)

    numberlist = [n]

    if (1 <= a <= 5000) and (1 <= b <= 5000) and (0 <= c <= 5000):
        while True:
            print(numberlist)
            if n == 1:
                break
            elif n % 2 == 0:
                n = int(n // 2)
                numberlist.append(n)
            else:
                n = int((n * 3) + 1)
                numb = int(b / 3)
                numberlist.append(n)
                if (n > numb) and (c > 0):
                    n += 10
                    c -= 1

    return len(numberlist)

print(num3plue1())
