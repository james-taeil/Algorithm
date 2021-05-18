def solution(S):
    S = S.split()

    numlist = []
    for i in S:

        #minus
        if i == '-':
            if len(numlist) < 2:
                answer = -1
                return answer
            else:
                minus = numlist[-1] - numlist[-2]
                numlist = numlist[:-2]
                numlist.append(minus)

        #plus
        elif i == '+':
            if len(numlist) < 2:
                answer = -1
                return answer
            else:
                plus = numlist[-1] + numlist[-2]
                numlist = numlist[:-2]
                numlist.append(plus)

        #duplicate
        elif i == 'DUP':
            numlist.append(numlist[-1])

        #pop
        elif i == 'POP':
            numlist = numlist[:-1]

        #int
        else:
            i = int(i)
            numlist.append(i)

    #result
    answer = numlist[-1]
    return answer


S = '3 DUP 5 - -'
print(solution(S))