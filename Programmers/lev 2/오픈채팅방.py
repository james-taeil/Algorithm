def solution(record):
    answer = []
    commands = []
    user_data = dict()
    
    for r in record:
        cmd, user_id = r.split(' ')[0], r.split(' ')[1]
        
        if cmd in ('Enter', 'Change'):
            name = r.split(' ')[2]
            user_data[user_id] = name
        commands.append((cmd, user_id))
        
    for command in commands:
        cmd, user_id = command[0], command[1]
        
        if cmd == 'Enter':
            answer.append(f'{user_data[user_id]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{user_data[user_id]}님이 나갔습니다.')
            
    return answer

def solution(record):
    answer = []
    names = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    
    for r in record:
        line = r.split(' ')
        
        if line[0] in ['Enter', 'Leave']:
            names[line[1]] = line[2]
        
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(names[r.split(' ')[1]] + printer[r.split(' ')[0]])
    
    return answer