n = int(input())
word = list(input())

for i in range(n - 1):
    other_word = list(input())
    
    for j in range(len(word)):
        if word[j] != other_word[j]:
            word[j] = '?'
  
print(''.join(word))