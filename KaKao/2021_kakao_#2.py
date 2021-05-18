from itertools import combinations
import collections

def solution(orders, course):
    answer = []
    for j in range(len(course)):
        n_list = []
        for i in orders:
            numlist = list(map(''.join, combinations(i, course[j])))
            n_list.extend(numlist)
            b = dict(collections.Counter(n_list))
            max_values = max(b.values())
            max_keys = [k for k, v in b.items() if v == max_values]
        if max_values <= 1:
            pass
        else:
            answer.extend(max_keys)
    return answer

print(solution( ["XYZ", "XWY", "WXA"],[2,3,5]))

#
#
#
# n_list = []
# for i in orders:
#     numlist = list(map(''.join, combinations(i, course[1])))
#     n_list.extend(numlist)
#     b = dict(collections.Counter(n_list))
#     max_values = max(b.values())
#     max_keys = [k for k, v in b.items() if v == max_values]
# answer.extend(max_keys)
#
# n_list = []
# for i in orders:
#     numlist = list(map(''.join, combinations(i, course[2])))
#     n_list.extend(numlist)
#     b = dict(collections.Counter(n_list))
#     max_values = max(b.values())
#     max_keys = [k for k, v in b.items() if v == max_values]
# answer.extend(max_keys)
