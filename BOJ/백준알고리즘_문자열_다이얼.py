# s = input().upper()
# num_sum = 0
# for i in s:
#     if i in "ABC":
#         num_sum += 3
#     elif i in "DEF":
#         num_sum += 4
#     elif i in "GHI":
#         num_sum += 5
#     elif i in "JKL":
#         num_sum += 6
#     elif i in "MNO":
#         num_sum += 7
#     elif i in "PQRS":
#         num_sum += 8
#     elif i in "TUV":
#         num_sum += 9
#     elif i in "WXYZ":
#         num_sum += 10
#     elif i == 1:
#         num_sum += 2
#     elif i == 0:
#         num_sum += 11
# print(num_sum)

strlist = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input().upper()
sum_number = 0
for i in range(len(s)):
    for j in strlist:
        if s[i] in j:
            sum_number = sum_number + strlist.index(j) + 3
print(sum_number)