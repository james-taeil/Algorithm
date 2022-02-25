def recursive(i):
    if i == 100:
        return
    
    print(i)
    recursive(i + 1)
    print(i, '번쨰 종료')
    
recursive(1)