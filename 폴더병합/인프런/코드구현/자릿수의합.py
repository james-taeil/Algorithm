'''
N개의 자연수가 입력되면 
자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수 출력
자릿수의 합 구하는 함수 만들기
'''

'''
코드 구현 생각
자릿수의 합?
'''

#숫자로 자리수 찾아서 하는 방법
def digit_sum(x):
    answer = 0
    total = []
    score = 0
    
    for i in x:
        while i > 0:
            score += i % 10
            i = i // 10
        total.append(score)
        score = 0
    
    max_num = 0
    for i in total:
        if i > max_num:
            max_num = i
            answer = x[total.index(i)]
    
    return answer

#문자열 방법
def solution(x):
    total = []
    sum = 0
    for i in x:
        for j in str(i):
            sum += int(j)
        total.append(sum)
        sum = 0
        
    max_num = 0
    for i in total:
        if i > max_num:
            max_num = i
            answer = x[total.index(i)]
            
    return answer
    #     sum += int(i)
    # print(sum)

num = [125, 15232, 97]
# print(digit_sum(num))
print(solution(num))