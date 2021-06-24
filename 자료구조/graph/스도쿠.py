# 문제
board = [
    [0, 3, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
  ]

# 스도쿠에서 0인 부분
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def is_promising(row, col):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        #row
        if board[row][k] in promising:
            promising.remove(board[row][k])
        #col
        if board[k][col] in promising:
            promising.remove(board[k][col])
            
    # 33박스 검사
    row //= 3
    col //= 3

    for i in range(row*3, (row+1)*3):
        for j in range(col*3, (col+1)*3):
            if board[i][j] in promising:
                promising.remove(board[i][j])
            
    return promising

#0 갯수가 x개 일때 까지        
def dfs(x):
    
    # 0을 값으로 채우는 과정
    ## 마지막 0까지 답으로 채웠을 경우
    if x == len(zeros):
        for row in board:
            print(*row)
    else :
        (i, j) = zeros[x]
        promising = is_promising(i, j) # 유망한 숫자 받기
        
        for num in promising:
            board[i][j] = num # 유망한 숫자 하나 넣기
            dfs(x + 1) #다음 0으로 넘어감
            board[i][j] = 0 #초기화
            

print(dfs(0))