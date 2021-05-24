#같은값 비교, 완전탐색
def solution(answers):
    answer = []
    supo = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    score = {1:0, 2:0, 3:0}

    for idx, value in enumerate(answers):
        for person, number in supo.items():
            if value == number[idx % len(number)]:
                score[person] += 1
                print(score)


    return answer

answers = [1,2,3,4,5]
print(solution(answers))