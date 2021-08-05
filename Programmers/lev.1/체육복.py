'''
1. reserve == 0 일때는 사람 수의 - lost 값 출력
2. reserve 의 수가 lost 보다 많을 경우
3. reserve 의 수가 lost 보다 적을 경우
4. 같을 경우
'''

def solution(n, lost, reserve):
    answer = n
    
    reverser = [i for i in reserve if i not in lost]

    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    
    for reserve_num in reserve:
        if  (reserve_num - 1) in lost:
            lost.remove(reserve_num - 1)
        elif (reserve_num + 1) in lost:
            lost.remove(reserve_num + 1)

    return answer - len(lost)

n = 30
lost = [28, 30]
reserve = [25, 27, 29]
print(solution(n, lost, reserve))
