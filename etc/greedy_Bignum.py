# a = input().split()
# listnumber = list(input().split())
# listnumber.sort(reverse=True)
#
# limt = int(a[2])
#
# sumnum = 0
#
# for i in range(1, int(a[1])+1):
#     if (i % (limt+1)) == 0:
#         sumnum = sumnum + int(listnumber[1])
#     else:
#         sumnum = sumnum + int(listnumber[0])
#
# print(sumnum)
# ----------------------------------------------------------------------

# n, m, k = map(int, input().split())
# numlist = list(map(int, input().split()))
#
# numlist.sort(reverse=True)
# first = numlist[0]
# second = numlist[1]
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# ----------------------------------------------


n, m, k = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()

first = numlist[-1]
second = numlist[-2]

#가장 큰 수
count = int(m / (k+1))*k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)