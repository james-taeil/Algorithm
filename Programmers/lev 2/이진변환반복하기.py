def solution(s):
    answer = [0, 0]
    count, zero = 0, 0
    while s != '1':
        remove = s.count('0')
        zero += s.count('0')
        s = bin(len(s) - remove)[2:]
        count += 1
    answer = [count, zero]
    return answer