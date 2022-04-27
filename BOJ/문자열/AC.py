from sys import stdin, stdout

def AC(commands, n, num_li):
    commands.replace('RR', '')
    l, r, d = 0, 0, True
    
    for command in commands:
        if command == 'R':
            d = not d
        elif command == 'D':
            if d:
                l += 1
            else:
                r += 1
    
    if l + r <= n:
        result = num_li[l : n  - r]
        
        if d: return '[' + ','.join(result) + ']\n'
        else: return '[' + ','.join(result[::-1]) + ']\n'
    else: return 'error\n'
            

T = int(stdin.readline())
for _ in range(T):
    commands = stdin.readline()
    n = int(stdin.readline())
    num_li = stdin.readline().rstrip()[1 : -1].split(',')
    
    if n == 0:
        []
    
    stdout.write(AC(commands, n, num_li))