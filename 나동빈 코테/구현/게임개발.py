n, m = map(int, input().split())

# 사용자가 움직일 수 있는 공간 0 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 

# 실제 맵
array = [];
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전해주는 함수
def turn_left():
    global direction
    direction -= 1
    # 북쪽을 바라볼때 0이어야 하니까 서쪽을 볼때 3으로 만들어 준다.
    if direction == -1:
        direction = 3

# 게임 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 육지일 경우 움직임
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # 네 방향이 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 가는 자표
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #바다로 막혀 있다면
        else:
            break
        turn_time = 0
        
print(count)
print(d)