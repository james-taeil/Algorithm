'''
1. 0으로 표시된 부분은 낙서된 부분 
최저 순위 : 낙서된 부분이 전부 아닌경우
최고 순위 : 낙서된 부분이 전부 맞은경우

2. 최저 순위 낙서 번호 가장 낮은 숫자 + 1
최고 순위 낙서 번호 가장 낮은 숫자로

3. 낙서 번호가 중복으로 넘어가는 경우
Ex)  1 2 3 4 5 6
     1 0 0 4 5 6
     
문제
연속으로 0이 들어갈때 또한 그 숫자가 이미 있을때,
해결
0을 다른 것으로 바꿔줄 필요가 없다, 0 있는 개수만큼 최대 개수로 더해주고, 최소 개수로 빼주면 댐
'''
#풀이
def solution(lottos, win_nums):
    answer = []
    
    lotto = {'1':6, '2':5, '3':4, '4':3, '5':2}
    
    lottos.sort()
    win_nums.sort()
    
    # zerocount = [i for i in lottos if i == 0]
    # print(len(zerocount))
    # correct = [i for i in lottos if i in win_nums]
    # print(len(correct))
    
    count = 0
    count_zero = 0
    for pick in lottos:
        if pick == 0:
            pass
        else:
            for win in win_nums:
                if pick == win:
                    count += 1                    
    
    for zero in lottos:
        if zero == 0:
            count_zero += 1
    
    for key, value in lotto.items():
        if (count + count_zero == 0) or (count + count_zero == 1):
            answer.append(6)
            break
        elif value == (count + count_zero):
            answer.append(int(key))
            break
    
             
    if count < 2:
            answer.append(int(6))
    else:
        for key, value in lotto.items():
            if value == count:
                answer.append(int(key))
                break
    
    return answer


lottos = [1,2,3,4,0,0]
win_nums = [5,6,7,8,9,10]
print(solution(lottos, win_nums))