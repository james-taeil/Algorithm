while True:
    io_num = input()
    
    if io_num == '0':
        break
    
    if io_num == io_num[::-1]:
        print('yes')
    else:
        print('no')