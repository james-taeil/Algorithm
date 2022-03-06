def insertSort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr

arr = [5, 4, 9, 0, 3, 2, 6, 7, 1, 8]
print(insertSort(arr))