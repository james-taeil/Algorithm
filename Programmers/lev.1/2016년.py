def solution(a, b):
    answer = ''
    weeks = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    months = {
        "1" : 31, "2" : 29, "3" : 31, "4" : 30, "5" : 31, "6" : 30,
        "7" : 31, "8" : 31, "9" : 30, "10" : 31, "11" : 30, "12" : 31
    }
    day = b
    for month, days in months.items():
        if str(a) != month:
            day += days
        elif str(a) == month:
            break
    idx = day % 7
    answer = weeks[idx]
    return answer

    # months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # return days[(sum(months[:a-1])+b-1)%7]
    

a = 5
b = 24
print(solution(a, b))

# 풀이 전략
# 달력 객체 만들기
# 요일 배열 만들기
# 배열 0번째 목요일 부터 시작
# 7로 나눈 나머지 값을 인덱스로 뽑으면 될 듯

# 개선점
# 어렵지 않으면 객체로 안뽑고 풀어도 된다...
# 슬라이스를 활용하면 쉬운 문제