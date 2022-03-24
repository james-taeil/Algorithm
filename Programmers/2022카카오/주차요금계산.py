from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    cars = []
    costs = []
    timeOfCar = defaultdict(list)
    defaultTime, defaultFee, unitTime, unitFee = fees
    
    # 시간 분으로 바꾸기
    def changeMinute(s):
        h, m = s.split(':')
        h = int(h) * 60
        m = int(m)
        
        return h + m
    
    # 차 번호 기준으로 인출 아웃 시간 만들기
    for record in records:
        time, carNumber, checkout = record.split(' ')
        timeOfCar[carNumber].append(changeMinute(time))            
        if carNumber in cars:
            continue
        else:
            cars.append(carNumber)
            
    # 아웃 없는 경우 23:59 넣어주기
    for car in cars:
        if len(timeOfCar[car]) % 2 == 1:
            timeOfCar[car].append(changeMinute('23:59'))
    
    # 시간 2개씩 계산해서 costs array 데이터 처리
    for car in cars:
        time = 0
        for i in range(0, len(timeOfCar[car]), 2):
            start, end = timeOfCar[car][i:i+2]
            time += int(end) - int(start)
            
        if time <= defaultTime:
            costs.append(defaultFee)
        else:
            print(defaultFee, time, defaultTime, unitTime, unitFee)
            costs.append(defaultFee + (math.ceil(((time - defaultTime) / unitTime)) * unitFee))
    
    answer = [x for _, x in sorted(zip(cars, costs))]
        
    return answer