#midium result
def solution(S):
    S = S.split()
    numlist = []

    for i in S:
        numlist.append(i)
    if len(numlist) % 2 == 1:
        mid = (numlist.index(numlist[-1]) + numlist.index(numlist[0])) // 2
        answer = numlist[mid]
    else:
        answer = "홀수갯수를 입력해 주세요."
    return answer
