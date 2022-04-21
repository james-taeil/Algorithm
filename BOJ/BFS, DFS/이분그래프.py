import queue
import sys
from collections import deque

sys.setrecursionlimit(20000)
input = sys.stdin.readline

# BFS
def bfs(start, group):
    queue = deque([start]) # 시작 Vertex
    visited[start] = group # 시작 정점 그룹을 설정
    
    while queue:
        x = queue.popleft() # 큐 시작
        
        for i in group[x]: # 해당 정점에서 갈 수 있는 하위 정점들 돌기
            if not visited[i]: # 해당 정점에서 방문하지 않았다면
                queue.append(i) # 정점 추가
                visited[i] = -1 * visited[x] # 상위 정점과 다른 그룹으로 편성
            elif visited[i] == visited[x]: # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False
              
    return True
    
for _ in range(int(input())):
    V, E = map(int, input().spilit())
    
    # 그래프 초기화
    graph = [[] for i in range(V + 1)]
    # 방문처리
    visited = [False] * (V + 1)
    
    for _ in range(E):
        a, b = map(int, input().split())
        # 무방향 그래프
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, V + 1):
        if not visited[i]: # 방문 정점이 아니라면 BFS 실행
            result = bfs(i, 1)
            if not result:
                break
              
    print('YES' if result else 'NO')