def solution(board, moves):
    answer = 0
    basket = list()
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                doll = board[j][i-1]
                if doll != 0:
                    basket.append(doll)
                board[j][i-1] = 0
                break
        if len(basket) <= 2:
            break
        elif (basket[-1] == basket[-2]):
            basket.pop()
            basket.pop()
            answer += 2

    return answer

if __name__ == '__main__':
    print(solution(board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves=[1,5,3,5,1,2,1,4]))
