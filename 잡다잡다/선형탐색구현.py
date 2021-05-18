def linear_search(element, some_list):
    # 코드를 작성하세요.
    count = 0
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
        else:
            count += 1
            if count == 5:
                return None

print(linear_search(2, [2, 3, 5, 7, 11])) #return 값 0
# print(linear_search(0, [2, 3, 5, 7, 11])) #return None
# print(linear_search(5, [2, 3, 5, 7, 11])) #return 2
# print(linear_search(3, [2, 3, 5, 7, 11])) #return 1
# print(linear_search(11, [2, 3, 5, 7, 11])) #retunr 4