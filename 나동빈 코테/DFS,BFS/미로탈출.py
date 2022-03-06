from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 넘는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인 경우
            if graph[nx][ny] == 0:
                continue
              
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        
    return graph
  
n, m = 5, 6

graph = [
  [1, 0, 1, 0, 1, 0],
  [1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1]
]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
print(BFS(0, 0))