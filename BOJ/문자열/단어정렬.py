line = int(input())
words = []

for i in range(line):
    word = str(input())
    words.append((word, len(word)))

# set 중복 삭제    
words = list(set(words))

# 단어 갯수 정렬, 알파벳 정렬
words.sort(key=lambda word: (word[1], word[0]))

for word in words:
    print(word[0])