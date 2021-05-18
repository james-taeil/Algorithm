#완주하지 못한 선수

def solution(participant, completion):
    d = {}
    for i in participant:
        d[i] = d.get(i, 0) + 1

    for i in completion:
        d[i] -= 1

    dnf = [k for k, v in d.items() if v > 0]

    answer = dnf

    return answer

"================================================="

def solution(participant, completion):
    participant.sort()
    completion.sort() 

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        return participant[len(participant)-1]