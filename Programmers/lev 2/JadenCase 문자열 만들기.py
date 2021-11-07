import re
def solution(s):
    answer = ''
    words = re.compile('[0-9][a-z]+').findall(s)
  
    print(words)
    return answer
  
s = "3people unFollowed me"
print(solution(s))