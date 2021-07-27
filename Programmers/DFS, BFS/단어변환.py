from collections import deque

def solution(begin, target, words):
    answer = 1
    QUEUE = deque()
    visited = [False for i in range(len(words))]
    QUEUE.append(begin)
    
    while QUEUE:
        for _ in range(len(QUEUE)):
            node = QUEUE.popleft()
            for idx in range(len(words)):
                if not visited[idx] and isCheckString(node, words[idx]):
                    if words[idx] == target:
                        return answer
                    QUEUE.append(words[idx])
                    visited[idx] = True
        answer += 1
 
    answer = 0
    return answer
        

# boolean type function
def isCheckString(fixStr, CheckStr):
    isSame = 2
    for i in range(len(fixStr)):
        if fixStr[i] != CheckStr[i]:
            isSame -= 1
    if isSame < 1:
        return  False
    return True
    


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", 'cog']
print(solution(begin, target, words))