#3이 넘으면 5키로 봉지로 3이 넘지 않으면 무조건 3키로로
#n의 초기값이 4일 경우가 가장 예외

# n = int(input())
# count = 0
#
# if n == 4:
#     count = -1
# else:
#     while True:
#         if n > 3:
#             #5킬로그램 설탕포대
#             n = n-5
#             count += 1
#         else:
#             #3킬로그램 설탕보대
#             n = n-3
#             count += 1
#         if n <= 0:
#             break
# #설탕포대
# print(count)

n = int(input())
count = 0

while True:
    if n % 5 == 0:
        n = n - 5
        count += 1
    else:
        n = n - 3
        count += 1

    if n < 0:
        count = -1
        break
    elif n == 0:
        break
print(count)
