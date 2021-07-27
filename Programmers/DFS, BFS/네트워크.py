def solution(n, computers):
    answer = 0
    visited = [False for i in range(len(computers))]
    for i in range(n):
        if not visited[i]: 
            visited[i] = True
            dfs(computers, i, visited)
            answer += 1
    return answer

def dfs (graph, v, visited):
    for i in range(len(graph[v])):
        if not visited[i] and graph[v][i] == 1:
            visited[i] = True
            dfs(graph, i, visited)

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
output = solution(n, computers)
print(output)
