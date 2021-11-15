import re
def solution(s):
    reg = re.compile('|w|D')
    print(reg.match('|w|D', s))
    print(reg)
    return

s = '123b4'
print(solution(s))