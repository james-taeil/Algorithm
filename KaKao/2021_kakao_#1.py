def solution(new_id):
    import re
    low_text = new_id.lower()

    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]', '', low_text)
    for i in range(100):
        if new_id.find('..', 0) == new_id.find('..'):
            new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    for i in range(100):
        if new_id == '':
            new_id += 'a'
        if len(new_id) >= 16:
            new_id = new_id[0:15]
            new_id = new_id.strip('.')
        if len(new_id) <= 2:
            new_id += new_id[-1]
            new_id = new_id.strip('.')
            if new_id == '':
                new_id += 'a'

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))