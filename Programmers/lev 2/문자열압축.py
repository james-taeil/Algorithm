def solution(s):
    answer = 999999
    if len(s) == 1:
        return 1
    
    for r in range(1, len(s)//2 + 1):
        result = ''
        count = 1
        word = s[:r]
        
        for i in range(r, len(s), r):
            if word == s[i:r+i]:
                count += 1
            else:
                if count == 1:
                    result += word
                else:
                    result += str(count) + word
                
                word = s[i:r+i]
                count = 1
        
        if count != 1:
            result += str(count) + word
        else:
            result += word
            
        answer = min(answer, len(result))
    return answer