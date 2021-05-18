'''
# 1. 입력받은 문자 소문자로 변경 >>> lower method
# 2. ".", "-", "_" 를 제외한 문자 모두 지우기 >>> 정규 표현식

정규 표현식
import re
re.sub('[ _.~!@#$%^&*()=+[{]}:?,<>/ ]', '', 인자) 함수를 만드는 기호나 괄호 같은 것은 \ 반드시 앞에 붙여야 한다.

# 3. "." 가 두번 이상 연속 된 부분을 "." 하나로 변환 lstrip rstrip 메소드
# 4. "." 가 문자 첫번째 위치나 마지막 위치에 있다면, 모두 제거한다.
# 5. 인자가 "" 이라면 return "a"를 해준다.
# 6. 정규표현식 된 문자가 16자 이상이라면 문자 앞 기준 15문자만 return 해주고 뒤에는 자른다.
# 7. #6에 문자를 15자로 했는데도 뒤에 "."가 있다면, 지워준다.
# 8. 인자의 문자열 길이가 2 이하 (1, 2) 라면 마지막 문자를 문자열 길이가 3이 될때까지
     마지막 문자를 반복해서 뒤에 붙여준다.
'''

정규화 써서 다시 풀어보기

import re

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]', '', new_id)
    new_id = new_id.lstrip(".").rstrip(".")
    
    
    if new_id == '':
        answer = 'a'
        return solution(answer)
    elif len(new_id) <= 2:    
        return solution(new_id + new_id[-1])
    elif len(new_id) == 3:
        return new_id
    
    
    new_id_str = ""
    for word in new_id:
        if len(new_id_str) == 0:
            new_id_str += word
        elif new_id_str[-1] =='.' and word == '.':
            pass
        else:
            new_id_str += word
            
    new_id = new_id_str
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    
    answer = new_id
    
    return answer
    
    

id = 'a..sd.fas...df...as..df.asdf...asdfasdf'
print(solution(id))