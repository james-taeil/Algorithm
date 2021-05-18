def solution(s):
    answer = 0

    string = ['zero', 'one', 'two', 'three', 'four', 
            'five', 'six', 'seven', 'eight', 'nine' ]
    idx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    new_list = []

    new_string = ""

    for i in zip(string, idx):
        new_list.append(i)
   

    # # while True:
    # for i in range(len(string)):
    #     if new_list[i][0] in s:
    #         new_string += new_list[i][1]
    #         temp = str(new_list[i][1])
    #         s = s[len(temp)-1:]
    #     elif new_list[i][1] in s:
    #         new_string += new_list[i][1]
    #         temp = str(new_list[i][1])
    #         s = s[len(temp)-1:]

    # answer = int(new_string)
    

    for i in s:
        for j in idx:
            if i == j:
                new_string += str(j)

            

    print(new_string)
    return answer

s = "223fourfour5sixsix77"
print(solution(s))