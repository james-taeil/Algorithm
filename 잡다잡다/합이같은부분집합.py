# DFS

import sys

def solution(n, arr):
    n = int(input())
    total = sum(arr)
    DFS(0, 0, arr)
    

def DFS(L, sum, arr):
    global total
    if sum > total//2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
    else:
        DFS(L+1, sum + arr[L])
        DFS(L+1, sum)


    
n = 6

arr = [1, 3, 5, 6, 7, 10]