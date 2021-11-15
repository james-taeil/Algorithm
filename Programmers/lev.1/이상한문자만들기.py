def solution(s):
    answer = ''
    arr = []
    s = s.split(' ')
    for string in s:
        temp = ''
        for i in range(len(string)):
            if i % 2 == 0:
                temp += string[i].upper()
            else:
                temp += string[i].lower()
        arr.append(temp)
    answer = ' '.join(arr)
    return answer

s = "try hello world"
print(solution(s))