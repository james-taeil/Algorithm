def binary_search(element, some_list):
    # 코드를 작성하세요.
    firstnum = some_list.index(some_list[0])
    lastnum = some_list.index(some_list[-1])
    pointer = (firstnum + lastnum // 2)






print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))