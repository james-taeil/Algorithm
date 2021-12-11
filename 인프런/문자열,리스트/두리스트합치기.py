def sumList(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr2)
    maxLength = min(len(arr1), len(arr2))
    p1 = p2 = 0
    
    while p1 < n and p2 < m:
        if arr1[p1] <= arr2[p2]:
            answer.append(arr1[p1])
            p1 += 1
        else:
            answer.append(arr2[p2])
            p2 += 1
    
    if p1 < n:
        answer.extend(arr1[p1:])
    else:
        answer.extend(arr2[p2:])
    
    return answer

arr1 = [1, 3, 5]
arr2 = [2, 3, 4, 6, 9, 9, 10]

print(sumList(arr1, arr2))