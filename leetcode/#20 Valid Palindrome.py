from collections import deque

def isPalindrome(self, s: str) -> bool:
        
        stack = deque()
        for string in s:
            if string.isalnum():
                stack.append(string.lower())

        while len(stack) > 1:
            if stack.popleft() != stack.pop():
                return False
        return True
