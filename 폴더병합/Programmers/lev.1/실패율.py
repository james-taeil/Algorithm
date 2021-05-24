'''
실패율
스테이지에 도달했으나 아직 클리어 하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

실패율이 높은 스테이지 수 부터 내림차순
1. 실패율 계산
2. 가장 높은 실패율 부터 값 내림차순
3. 같은 실패율일 경우 스테이지 오름차순
'''
import collections

def solution(N, stages):
    answer = []
    
    stagesCount = {}
    
    for i in range(1, N + 1):
        stagesCount[i] = stagesCount.get(i, 0)
    
    for stage in stages:
        if stage > N:
            pass
        else:
            stagesCount[stage] = stagesCount.get(stage, 0) + 1
        
    stagesCount = dict(sorted(stagesCount.items()))
    
    fail = 0
    success = len(stages)
    failRate = {}
    
    for key, value in stagesCount.items():
        success -= fail
        fail = value
        failRate[key] = fail/success

    
    failSort = sorted(failRate.items(), reverse=True, key=lambda x : x[1])
    print(failSort)
    
    for i in failSort:
        answer.append(i[0])
    
    return answer


print(solution(N=5, stages=[2, 1, 2, 6, 2, 4, 3, 3]))


# d = {}
# for i in participant:
#     d[i] = d.get(i, 0) + 1

# for i in completion:
#     d[i] -= 1

# dnf = [k for k, v in d.items() if v > 0]

# answer = str(dnf[0])