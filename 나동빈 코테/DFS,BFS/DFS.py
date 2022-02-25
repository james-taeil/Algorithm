def DFS(graph, value, visited):
    visited[value] = True
    print(value, end=' ')
    
    for i in graph[value]:
        if not visited[i]:
            DFS(graph, i, visited)
            
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

DFS(graph, 1, visited)