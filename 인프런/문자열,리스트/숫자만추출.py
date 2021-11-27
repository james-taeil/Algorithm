'''
영어와 숫자가 섞여있는 문자열이 있을때
문자열 중 숫자만 추출하여 출력
##앞 자리가 0일 경우 무시
그리고 약수를 구하기
'''


'''
코드 구현 생각
for 문으로 숫자 탐색해서 한 리스트에 담기
첫번째 부터 0인지 확인 후 0이면 슬라이스
약수 구하기
'''
import re

def solution(s:str):
    p = re.compile('[0-9]+')
    m = int(''.join(p.findall(s)))
    
    # 약수 갯수
    # sum = 0
    
    # for i in s:
    #     if i.isdigit():
    #         sum = (sum * 10) + int(i)
    # print(sum)
    
    count = 0
    
    for i in range(1, m + 1):
        if m % i == 0:
            count += 1
    
    return count


s = "gasd0asdfh2asdf8asdfg"
print(solution(s))