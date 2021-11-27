def solution(score):
    answer = 0
    count = 0
    for i in score:
        if i == 1:
            count += 1
            answer += count
        else:
            count = 0
    
    return answer


score = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
print(solution(score))