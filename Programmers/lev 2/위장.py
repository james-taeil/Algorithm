def solution(clothes):
    answer = 1;
    obj = dict()
    
    for clothe, type in clothes:
        obj[type] = obj.get(type, 0) + 1
    
    for key in obj:
        answer *= (obj[key] + 1)
        
    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))