'''
회문 문자열
한 거점을 놔두고 앞뒤가 같은 패턴이다.
'''

'''
코드 구현 생각
for 문 돌려서 앞문자와 맨 뒷문자 비교
'''


s = ['level', 'soon', 'google', 'lol', 'Lol']
for j in s:
    string = j.lower()
    size = len(string)
    for k in range(size//2):
        if string[k] != string[-1-k]:
            break
    else:
        print(j, 'is True')

    #if j == j[::-1]