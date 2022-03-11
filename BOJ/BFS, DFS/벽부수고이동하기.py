import sys
from collections import deque

input = sys.stdin.readline()
n, m = map(int, input().split())
board = [list(map(int, input().rsplit())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    
    while queue:
        r, c, wall = queue.popleft()
        
        if r == n - 1 and c == m - 1:
            return visited[r][c][wall]
        
        for i in range(4):
            nr = r + DIR[i][0]
            nc = c + DIR[i][1]
            
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][wall] == 0:
                if board[nr][nc] == 0:
                    queue.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                    
                if wall == 0 and board[nr][nc] == 1:
                    queue.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][wall] + 1
    return -1

print(bfs())
    