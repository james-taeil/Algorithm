n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            board.append(count)
            count = 0
            
print(len(board))
board.sort()

for i in board:
    print(i)