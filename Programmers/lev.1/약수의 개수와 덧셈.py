# def isPrime (num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     return count
        

# def solution(left, right):
#     answer = 0
#     for i in range(left, right + 1):
#         count = isPrime(i)
#         print(i**0.5, int(i**0.5))
#         if count % 2 == 0:
#             answer += i
#         else:
#             answer -= i
#     return answer

#     # answer = 0
#     # for i in range(left,right+1):
#     #     if int(i**0.5)==i**0.5:
#     #         answer -= i
#     #     else:
#     #         answer += i
#     # return answer

# print(solution(left = 13, right = 17))


# 풀이전략
# 약수를 찾는 함수 만들기
# 약수 일때라면 count + 1씩 해주기
# 반복문 돌면서 파라미터 범위내에 값 약수 갯수 판별하기
# 약수의 개수가 짝수라면 현재 값을 answer에 더해주고
# 홀수라면 빼주기

# 개선점
# 제곱수로 할 수 있는 방법이 있다.
# 제곱수를 좀 더 공부하자
# 약수개수가 홀수인 친구들은 루트 하면 소수점이 나오고
# 아닌 친구들은 정수가 나옴


# 에라토스테네스의 체
def aratos(num):
    aratos = [0 for i in range(num + 5)]
    aratos[1] = 1
    for i in range(2, num + 1):
        if aratos[i] == 0:
            p = 2
            while p*i <= num:
                aratos[p*i] = 1
                p += 1
                
    return aratos[num]

print(aratos(15))