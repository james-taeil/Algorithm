strings = input()
alphabet = [0] * 26

for i in range(len(strings)):
    idx = ord(strings[i]) - 97
    alphabet[idx] += 1
    
for i in range(len(alphabet)):
    print(alphabet[i], end=' ')