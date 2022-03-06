def selectSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i + 1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        
    return arr
  
arr = [5, 4, 9, 0, 3, 2, 6, 7, 1, 8]
print(selectSort(arr))