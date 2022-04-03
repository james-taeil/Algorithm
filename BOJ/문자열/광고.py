import sys

# failure : 본문에서 F배열을 리턴하는 함수
def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

# 입력 및 정답 출력
n = int(sys.stdin.readline())
pat = sys.stdin.readline().rstrip()
print(n - failure(pat)[n - 1])