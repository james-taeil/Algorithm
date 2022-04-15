import re


n = int(input())
m = int(input())

graph = [[] * n for _ in range(n + 1)]

# make node
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(graph)

visited = [0] * (n + 1)
result = 0

def dfs(start):
    global result
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            result += 1
            
dfs(1)
print(result)