'''
두 N면체 주사위를 던져서 두 누 눈의 합 중 가장 
확률이 높은 숫자를 출력
'''

'''
코드구현 생각
행렬로 생각
count = {}로 하여 각각 key의 값이 몇번 등장하였는지
찾으면 된다.
그중 가장 많이 등장한 숫자가 가장 높은 확률의 숫자이다. 

중복이 문제
'''
N = 4
M = 6
cnt = [0]*(N+M+2)
max_number = 0
for first_number in range(1, N+1):
    for second_number in range(1, M+1):
        # cnt.append(first_number + second_number)
        cnt[first_number + second_number] += 1

print(cnt)

for i in range(N+M+1):
    if cnt[i]>max_number:
        max_number = cnt[i]

for i in range(N+M+1):
    if cnt[i] == max_number:
        print(i, end=' ')
# for idx, value in enumerate(cnt):