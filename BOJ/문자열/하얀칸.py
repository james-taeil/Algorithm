chess = []

for _ in range(8):
    chess.append(list(map(str, input())))
    
answer = 0

# 짝수 칸이 흰색칸
# 그 중 F 있는 칸 갯수만 카운트
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] == 'F':
                answer += 1

print(answer)