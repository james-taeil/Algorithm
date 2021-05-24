def solution(participant, completion):
    answer = ''

    d = {}
    for i in participant:
        d[i] = d.get(i, 0) + 1
    
    for i in completion:
        d[i] -= 1
    
    dnf = [k for k, v in d.items() if v > 0]

    answer = str(dnf[0])

    return answer

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))


# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     retrun list(answer.keys())[0]