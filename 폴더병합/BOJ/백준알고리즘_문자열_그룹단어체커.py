#그룹단어경우
#1. 서로 다른단어
#2. 같은단어가 연속으로 나올때
#///
#그룹단어가 아닌경우
#같은단어가 연속으로 나오지 않을떄 /// 즉 띄어져서 나올때

s = int(input())
count = 0
for i in range(s):
    word = input()
    if len(word) == 1: #단어가 1개 일때
        count += 1
    else:
        for j in range(len(word)-1):
            if j != len(word)-2: #문자열 끝까지 비교
                if word[j] == word[j+1]: #두문자 같을때
                    pass
                elif word[j] in word[j+1:]: #두문자다를때// 연속으로 나오지 않을때 체크
                    break
            else: #문자열 비교 후 검수가 끝나면 횟수 카운트
                count += 1
print(count)

# 단어에서 두 글자씩을 비교하여 앞 글자가 처음 등장하는 인덱스보다
# 뒷 글자가 처음 등장하는 인덱스가 더 작으면, 뒷 글자는 앞서 이미 등장한 글자가 됩니다.
# 따라서 그룹 단어가 아니므로, 결과에서 1을 제외하고 다음 단어를 검사합니다.


# s = int(input())
# count = 0
# for i in range(s):
#     word = input()

