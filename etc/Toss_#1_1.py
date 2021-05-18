import copy

a, b, c = input().split()


def solution(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    c_copy = copy.deepcopy(c)

    # print(a)
    # print(b)
    # print(c)

    # count = 0
    # count_copy = copy.deepcopy(count)
    # 최대 사이클의 길이 구하기

    n_list = []
    count_list = []

    # n이 될수 있는 리스트를 만듭니다.
    for i in range(a, b + 1):
        n_list.append(i)
        # print(n_list, "n_list") # 22 22 3 -> [22]

    for i in range(len(n_list)):
        count = 1
        n = n_list[i]

        # print(n)
        c = c_copy
        # print(c)
        while n != 1:
            # print(c)
            if n % 2 == 0:
                n = n / 2
                count += 1

            else:
                n = n * 3 + 1
                count += 1
                if n > b / 3 and c > 0:
                    n += 10
                    c -= 1

        count_list.append(count)

    return max(count_list)


print(solution(a, b, c))