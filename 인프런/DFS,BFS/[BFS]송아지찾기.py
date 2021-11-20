from collections import deque

def BFS(n, m):
    MAX = 10000;
    visited = [False] * (MAX + 1)
    dis = [0] * (MAX + 1)
    visited[n] = True
    dis[n] = 0
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == m:
            break
        for next in (now - 1, now + 1, now + 5):
            if 0 < next <= MAX:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    dis[next] = dis[now] + 1
    return dis[m]
    
# 출발값
n = 5

# 도착값
m = 14

print(BFS(n, m))
