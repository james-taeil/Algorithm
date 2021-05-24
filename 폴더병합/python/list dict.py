def solution(my_list):
    list_dict = {}
    for idx in my_list:
        try:
            list_dict[idx] += 1
        except:
            list_dict[idx] = 1
    return list_dict


one_list = ["one", 2, 3, 2, "one"]
print(solution(one_list))