# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수,
# solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
#
# 제한 사항
# str은 길이 1 이상인 문자열입니다.
# 입출력 예
# s	return
# Zbcdefg	gfedcbZ

import re
#아스키 코드 소문자 097-122 // 대문자 065 - 090
#

def solution(s):
    answer = ''
    intlist = []
    low_str = []
    up_str = []

    #문자 찾아서 아스키코드 값으로
    for i in range(len(s)):
        intlist.append(ord(s[i]))

    #정렬
    intlist.sort()

    #소문자 대문자 구분 대문자 아스키 코드 65-90 // 소문자 97-122
    #소문자 우선으로 구분
    for k in intlist:
        if k <= 122 and k >= 97:
            low_str.append(k)
        else:
            up_str.append(k)

    #소문자 뒤 대문자 넣기
    low_str.extend(up_str)

    #아스키코드 값 문자료 변환
    for j in low_str:
        answer = answer + chr(j)
    return answer


# s = 'Zbcdefg'
# s = 'APSpasdfoza'
s = 'AZasdfASDFZCVasa'

print(solution(s))