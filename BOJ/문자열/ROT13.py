sentence = input()
answer = ''

for s in sentence:
    if s.islower():
        print(chr(97 + (ord(s) + 13 - 97)% 26), end='')
    elif s.isupper():
        print(chr(65 + (ord(s) + 13 - 65)% 26), end='')
    else:
        print(s, end='')
    