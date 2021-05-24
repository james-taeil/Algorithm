# def solution(numbers):
#     answer = []

#     numbers.sort()

#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             twosum = (numbers[i] + numbers[j])
#             if twosum in answer:
#                 pass
#             else:
#                 answer.append(twosum)
#     answer.sort
#     return answer




def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            twosum = (numbers[i] + numbers[j])
            answer.append(twosum)

    return sorted(list(set(answer)))

num = [2,1,3,4,1,7,8,9,10,11,12,13,14,15,16,17]
print(solution(num))