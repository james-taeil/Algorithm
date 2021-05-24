'''
N명의 학생의 평균을 구하고 평균에 가장 가까운 학생은 몇번째 학생인지
출력 하는 프로그램 
반올림 할 것
'''

'''
코드 구현 생각

N명의 학생 점수 합산 하여 평균 구하고, sum/n
앞 뒤로 점수 찾아서 합하고 나누기 2하여 평균값*2와 같다면 큰값 출력
아니면 제일 가까운 값 찾기
가까운 값은 평균값에서 앞뒤 값 빼보고 작은 값으로 정한다.
'''
# 9 10 11 12 13 14
N = [9, 10, 11, 12, 13, 15]

#round 소수 첫째자리 반올람
avg_score = sum(N)/len(N)
score_min = 2147000000
for idx, value in enumerate(N):
    temp = abs(value - avg_score)
    if temp < score_min:
        score_min = temp
        score = value #현재 인덱스에 있는 학생 점수
        result = idx + 1 #현재 점수 학생의 인덱스

    elif temp == score_min:
        if value > score:
            score = value
            result = idx + 1
print(avg_score, result)
# for scroe in N:

#     point_number.append(abs(avg_scorce-score))

# if len(point_number) >= 3:
#     print(N[N.index(avg_scorce)])
# else:
#     print(point_number)


'''
내가 푼 풀이와 다른점
1. 굳이 리스트 안써도 된다.
2. 버리는 값을 잘 알아야한다.
'''