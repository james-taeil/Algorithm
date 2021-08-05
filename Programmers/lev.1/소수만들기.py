from itertools import combinations
import math
# def combination(arr, r):
#     # 1.
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     # 2.
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#     	# 3.
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
#                 chosen.append(arr[nxt])
#                 used[nxt] = 1
#                 generate(chosen)
#                 chosen.pop()
#                 used[nxt] = 0
#     generate([])
    
# def combination(arr, selectnumber):
#     for i in range(len(arr)):
#         if selectnumber == 1:
#             yield [arr[i]]
#         else:
#             for j in combination(arr[i+1:], selectnumber-1):
#                 yield [arr[i]] + j

# O(n ^ 1/2)
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# O(nlogn)
# def isPrime(num):
#     array = [True for i in range(num + 1)]
    
#     # 에라토스테네스의 체
#     # 2부터 n제곱근 까지 모든 수 확인
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if array[i] == True:
#             j = 2
#             while i * j <= num:
#                 array[i * j] = False
#                 j += 1
#     return [i for i in range(2, num + 1) if array[i]]

def solution(nums):
    answer = 0
    nums.sort()
    combi = list(combinations(nums, 3))
    
    for i in range(len(combi)):
        if isPrime(sum(combi[i])):
            answer += 1
    return answer



nums = [1, 4, 3, 2, 5]
print(solution(nums))


# 풀이 전략
# 순열을 구현하기
# 값 3개를 선택하기
# 값 3개를 선택한 순열 값의 합을 구하여 소수인지 판별

# 개선점
# 제너레이터 공부
# yield 공부

