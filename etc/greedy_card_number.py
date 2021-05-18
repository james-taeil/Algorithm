# n, m = map(int, input().split())
# count = 0
# result = 0
#
# while True:
#     row = list(map(int, input().split()))
#     if len(row) == m:
#         row.sort()
#         if result <= row[0]:
#             result = row[0]
#
#         count += 1
#         if count == n:
#             break
#
# print(result)
#------------------------------------------------

n, m = map(int, input().split())

result = 0

for i in range(n):
    row = list(map(int, input().split()))
    min_value = min(row)
    result = max(result, min_value)
    print(result)

#---------------------------------------------------

# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     row = list(map(int, input().split()))
#
#     min_value = 10001
#     for j in row:
#         min_value = min(min_value, j)
#
#     result = max(result, min_value)
#
# print(result)