def check(s):
    stack = []
    
    for i in s:
        if i in ('[', '(', '{'):
            stack.append(i)
        else:
            if not stack:
                return False
            x = stack.pop()
            if i == ']' and x != '[':
                return False
            elif i == ')' and x != '(':
                return False
            elif i == '}' and x != '{':
                return False
    if stack:
        return False
    return True
            
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        if i != 0:
            s = s[1:] + s[0]
        if check(s) == True:
            answer += 1
    return answer

        
s = "[](){}"
print(solution(s))