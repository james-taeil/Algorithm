def in_range(x, y):
    SIZE = 5
    return -1 < x < SIZE and -1 < y < SIZE
 
 
def check(r, c, p):
    dist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == 'P':
            return False
        
    dist = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == "P" and (p[r][ny] != "X" or p[nx][c] != "X"):
            return False
 
    dist = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == "P" and p[r + dx // 2][c + dy // 2] != "X":
            return False
        
    return True
 
 
def solution(places):
    answer = []
    entire_matrix = [(i, j) for i in range(5) for j in range(5)]
    print(entire_matrix)
    for place in places:
        for r, c in entire_matrix:
            if place[r][c] == 'P' and not check(r, c, place):
                answer.append(0)
                break
        else:
            answer.append(1)
 
    return answer

palces = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(palces)

# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(place, person):
#     visited = [[False] * 5 for _ in range(5)]
#     count = 0
#     q = deque()
#     q.append(person)
#     while q:
#         for _ in range(len(q)):
#             y, x = q.popleft()
#             visited[y][x] = True
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[ny][nx]:
#                     continue
#                 if place[ny][nx] == 'P':
#                     return False
#                 elif place[ny][nx] == 'X':
#                     continue
#                 else:
#                     q.append((ny, nx))
                    
#         count += 1
#         if count == 2 or not q:
#             return True

# def solution(places):
#     ans = []
#     for place in places:
#         people = deque()
#         for i in range(5):
#             for j in range(5):
#                 if place[i][j] == 'P':
#                     people.append((i, j))
                    
#         if len(people) == 0:
#             ans.append(1)
#             continue
        
#         flag = True
#         print(people)
#         for person in people:
#             if not bfs(place, person):
#                 flag = False
#                 break
        
#         if not flag:
#             ans.append(0)
#         else:
#             ans.append(1)
        
#     return ans
