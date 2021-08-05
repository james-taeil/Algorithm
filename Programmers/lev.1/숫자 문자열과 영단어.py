def solution (s):
    words = {
        "zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four": 4, "five" : 5,
        "six" : 6, "seven": 7, "eight": 8, "nine": 9
    }
    answer = s
    for word in words:
        if word in s:
            number = str(words[word])
            answer = answer.replace(word, number)
            
    # for key, value in words.items():
    #     answer = answer.replace(key, value)        
            
    return int(answer)



s = "one4seveneight"
print(solution(s))

# 풀이 전략
# 영단어 숫자 객체를 만들어주기
# 파라미터로 받은 인자안에 영단어를 객체 키로 찾기
# 맞은 경우 replace를 사용하여 키의 값으로 바꿔주기


# 개선점
# for문에서 items()로 하면 더 쉽다....
# key value로 다 뽑을 수가 있다...