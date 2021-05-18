def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for line in board:
            if line[move-1] != 0:
                doll = line[move-1]
                basket.append(doll)
                line[move-1]
                break
    
        if len(basket) > 1 and basket[-2] == basket[-1]:
            basket = basket[:-2]
            answer += 2
    return answer

board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))