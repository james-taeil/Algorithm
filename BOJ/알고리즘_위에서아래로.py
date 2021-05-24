n = int(input())
numlist = []
for i in range(n):
    s = int(input())
    numlist.append(s)

#선택 정렬
# for i in range(len(numlist)):
#     min_index = i
#     for j in range(i + 1, len(numlist)):
#         if numlist[min_index] > numlist[j]:
#             min_index = j
#     numlist[i], numlist[min_index] = numlist[min_index], numlist[i]

#퀵정렬
# def quick_sort(numlist):
#     if len(numlist) <= 1:
#         return numlist
#
#     pivot = numlist[len(numlist)//2]
#     left, equal, right = [], [], []
#
#     for num in numlist:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(left) + equal + quick_sort(right)

def quick_sort(numlist, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and numlist[left] <= numlist[pivot]:
            left += 1
        while right > start and numlist[right] >= numlist[pivot]:
            right -= 1

        if left > right:
            numlist[right], numlist[pivot] = numlist[pivot], numlist[right]
        else:
            numlist[left], numlist[pivot] = numlist[pivot], numlist[left]
    quick_sort(numlist, start, right - 1)
    quick_sort(numlist, right + 1, end)

    return numlist


print(quick_sort(numlist, 0, len(numlist) - 1))