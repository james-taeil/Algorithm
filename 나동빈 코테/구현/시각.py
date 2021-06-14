# n 을 입력 받으면 00시 00분 00초 ~ n시 59분 59초 중 3인 숫자가 포함된
# 시간을 모두 카운팅

# 3중 반복문으로 단순 새기?
# 초에 3이 있을 경우 새기
# 분에 3이 있을 경우 새기
# 시에 3이 있을 경우 새기

n = int(input())
count = 0

# for hour in range(0, n+1):    
#     for mit in range(0, 60):
#         for sec in range(0, 60):
#             if (hour % 10 == 3) or (mit // 10 == 3) or (mit % 10 == 3) or (sec // 10 == 3) or (sec % 10 == 3):
#                 count += 1        
    
# print(count)


## 정답 해설

for hour in range(n + 1):
    for mit in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(mit) + str(sec):
                count += 1

print(count)