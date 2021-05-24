'''
영어와 숫자가 섞여있는 문자열이 있을때
문자열 중 숫자만 추출하여 출력
##앞 자리가 0일 경우 무시
그리고 약수를 구하기
'''


'''
코드 구현 생각
for 문으로 숫자 탐색해서 한 리스트에 담기
첫번째 부터 0인지 확인 후 0이면 슬라이스
약수 구하기
'''

s = "gasd0asdfh8asdf87asdf7g2"

string = 0

for i in s:
    if i.isdecimal():
        string = string * 10 + int(i)
        
cnt = 0

for i in range(1, string+1):
    if string%i == 0:
        cnt += 1

print(string, cnt)