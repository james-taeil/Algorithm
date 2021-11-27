def reversCard(start, end):
    answer = []
    cards = list(range(21))
    
    for i in range((end - start + 1) // 2):
        cards[start + i], cards[end - i] = cards[end - i], cards[start + i]
    return cards

start = 5
end = 10
print(reversCard(start, end))