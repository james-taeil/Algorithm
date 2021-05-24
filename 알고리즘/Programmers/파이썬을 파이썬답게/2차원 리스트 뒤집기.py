
'''
다음을 만족하는 함수, solution을 완성해주세요.
solution 함수는 이차원 리스트, mylist를 인자로 받습니다
solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, 
slution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.
'''

def solution(mylist):
    answer = [[]]
    new_list = []
    
    for i in range(len(mylist)):
        new_list.append([])

    for line in range(len(mylist)):
        for degree in range(len(mylist)):
            new_list[line].append(mylist[degree][line])
    answer = new_list
    return answer

    answer = [[]]

    # new_list = list(map(list, zip(*mylist)))
    new_list = []

    # for line in zip(*mylist):
    #     for degree in line:
            


            

    answer = new_list

    return answer


    '''
    print(new_id)
mylist = [[0, 3, 1, 2], [1, 1, 3, 4], [0, 3, 1, 3], [3, 0, 3, 1]]

print(solution(mylist))

'''
입력값	[[0, 3, 1, 2], [1, 1, 3, 4], [0, 3, 1, 3], [3, 0, 3, 1]]
기댓값	[[0, 1, 0, 3], [3, 1, 3, 0], [1, 3, 1, 3], [2, 4, 3, 1]]
'''