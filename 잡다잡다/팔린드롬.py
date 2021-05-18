def is_palindrome(word):
    wordlist = ''
    reverslist = ''
    for i in word:
        wordlist += i
    for j in reversed(word):
        reverslist += j

    if wordlist == reverslist:
        return True
    else:
        return False
    # 코드를 입력하세요.


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))