n = int(input())

for _ in range(n):
    sentence = input().split(' ')
    
    for sent in sentence:
        print(sent[::-1], end=" ")