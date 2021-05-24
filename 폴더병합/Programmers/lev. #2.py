def solution(s):
    wordlist = []
    lenword = len(s)

    if (lenword % 2) == 1:
        wordindex = lenword // 2

        answer = s[wordindex]

    else:
        wordindex = lenword // 2 - 1
        answer = s[wordindex:wordindex+2]

    return answer

print(solution('abcde'))