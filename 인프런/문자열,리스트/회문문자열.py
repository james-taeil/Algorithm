'''
회문 문자열
한 거점을 놔두고 앞뒤가 같은 패턴이다.
'''

'''
코드 구현 생각
for 문 돌려서 앞문자와 맨 뒷문자 비교
'''
def solution(s):
    answer = {}
    for i in s:
        i = i.lower()
        # 파이썬 경우 string reverse 는 slice로 가능하다
        
        # if i == i[::-1]:
        #     answer[i] = True
        # else:
        #     answer[i] = False
        
        size = len(i)
        for j in range(size // 2):
            if i[j] != i[-1 - j]:
                answer[i] = False
                break
        else:
            answer[i] = True
    
    return answer

s = ['level', 'soOn', 'Google', 'lol', 'Lol', 'Kakao', 'notBad', 'gOoOoooOg']
print(solution(s))