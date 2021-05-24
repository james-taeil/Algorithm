a, b, c = map(int, input().split())

# a = 기본 투자 비용(고정비용), b = 한대 판매시이익(가변비용), c = 노트북 가격
# a + (b*n) = 총 비용 /// #n = 노트북 대수

BREAK_EVEN_POINT = 0

#끝나지 않는 경우
if b >= c:
    BREAK_EVEN_POINT = -1
else:
    BREAK_EVEN_POINT = (a // (c-b)) + 1
print(BREAK_EVEN_POINT)

