# def solution(array, commands):
#     answer = []

#     for i in range(len(commands)):
#         numsort = []
#         numsort = array[commands[i][0]-1:commands[i][1]]
#         numsort.sort()
#         answer.append(numsort[commands[i][2]-1])
#     return answer


def solution(array, commands):
    answer = []

    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))