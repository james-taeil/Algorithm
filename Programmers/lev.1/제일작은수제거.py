def solution(arr):
    if len(arr) < 1:
        return [-1]
    else:
        arr.remove(min(arr))
    return arr

arr = [10]
print(solution(arr))