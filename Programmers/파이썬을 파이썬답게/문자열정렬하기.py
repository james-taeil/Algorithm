s, n = input().strip().split(' ')

n = int(n)

temp = int(n - len(s))

answer = ""
#좌측정령
answer += s
for i in range(temp):
    answer += ' '
print(answer)

#중앙정렬
answer = ""
for i in range(int(temp/2)):
    answer += " "
answer += s
for i in range(int(temp/2)):
    answer += " "
print(answer)


answer = ""
#우측정렬
for i in range(temp):
    answer += ' '
answer += s
print(answer)