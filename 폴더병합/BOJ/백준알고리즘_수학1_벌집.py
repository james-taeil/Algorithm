n = int(input())

room = 1
firstnum = 7
plus = 6
while True:
    #1번째 방인 경우
    if n == 1:
        break
    #2번째 방인 경우
    if n <= firstnum:
        room += 1
        break
    #3번째 이상부터 7에 +6씩 계속 증가해준다.
    else:
        plus += 6
        firstnum += plus
        room += 1
print(room)


room = 1
plue = 6
num = 1
n = int(input())
while True:
    if n > num:
        num += plue
        plue += 6
        room += 1
        continue
    break
print(room)