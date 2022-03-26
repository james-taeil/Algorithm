import re

reg = re.compile(r'[a-zA-Z0-9-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\s]+')
reg = re.compile(r'[0-9-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')

s = 'abc123'  # 검색하려는 문자열.
m = re.match('abc', s) # 문자열에 맞는 패턴이 있는지 확인, 여기서는 abc가 패턴
print(m.group()) # 일치하는 패턴이 있는 경우 m에 값이 담겨 있고, group을 쓰면 일치하는 문자열이 출력됨
abc # 출력결과

s = 'abcd1004'
m = re.match('a.c', s) # a.c와 일치하는 문자열을 찾는다. 
print(m.group())
abc # 출력결과

s = '123abc456'
m = re.match('a.c', s)
print(m) # 출력결과 : None

s = '123abc456'
m = re.search('abc', s)
print(m.group()) # 출력결과 : abc

s = '123def789' # 검색 대상인 문자열
m = re.search('[a-f]e', s) # [a-f] 는 a~f까지, abcdef 중 일치하는 게 하나라도 있는지 확인한다는 뜻
print(m.group())

s = 'hello-world-123-good-984'
m = re.search('[a-zA-Z]+',s) # [a-zA-z]는 모든 알파벳을 뜻함. +는 1개 이상 일치하는 문자열이 있는 경우.
print(m.group()) # 실행결과 : hello

s = 'hello-world-123-good-984'
m = re.findall('[a-zA-Z]+',s)
print(m) # 출력결과 ['hello', 'world', 'good']

# 메타문자
s = '0aaa5'
m = re.search('a{3,4}', s) # a{3,4}는 범위를 나타내는 정규식. a가 3번이상이고 4번 이하면 맞는 패턴으로 본다
print(m.group()) # 출력결과 : aaa

s1 = '휴대전화에요.010-1234-9001'
m1 = re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}', s1) 
print(m1.group()) # 출력결과 : 010-1234-9001

s2 = '중국집이에요.02-2940-7001'
m2 = re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}', s2)
print(m2.group()) # 출력결과 : 02-2940-7001

s = '안녕하세요. 좋은 아침이에요'
m = re.search('^안녕', s)
print(m.group()) # 출력결과 : 안녕

s = '좋은 아침이에요.안녕하세요'
m = re.search('^안녕', s)
print(m) # 출력결과 : None

s = '지금은 즐겁게 있어요'
m = re.search('[ㄱ-힣]+요$', s) # [ㄱ-힣] 은 한글일때만 일치하는 걸로 본다는 뜻
print(m.group()) # 출력 결과 : 있어요

s = 'There is a crow and bird'
m = re.findall('cro*w|bir+d', s) # | 앞뒤로 정규식이 2개 있다
print(m) # 출력결과 : ['crow', 'bird']

s = '안녕하세요. 새해 복 많이 받으세요. 글은 2021-01-06에 썼어요'
m = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', s) # 날짜를 찾기 위함. 
print(m.group()) # 출력결과 : 2021-01-06

s = '안녕하세요. 새해 복 많이 받으세요. 글은 2021-01-06에 썼어요'
m = re.search('([0-9]{4})-([0-9]{2})-([0-9]{2})', s) # ()로 세번 묶어줌. 
print(m.group(0)) # 출력결과 : 2021-01-06
print(m.group(1)) # 출력결과 : 2021
print(m.group(2)) # 출력결과 : 01

s = '오늘은 안녕하세요.안녕하세요?'
m1 = re.search('안녕하세요\?', s)
print(m1.span()) # span은 일치하는 범위를 말함. span - (10, 16)
print(m1.group()) # 출력결과 : 안녕하세요?

m2 = re.search('안녕하세요?', s)
print(m2.span()) # span - (4, 9), 위와는 span이 다르다. 
s = 'Ryan has sent an invoice email to john.d@yahoo.com by using his email id ryan.arjun@gmail.com and he also shared a copy to his boss rosy.gray@amazon.co.uk on the cc part.'

m = re.findall(r'[\w\.-]+@[\w\.-]+', s)
print(m) # 출력 결과 : ['john.d@yahoo.com', 'ryan.arjun@gmail.com', 'rosy.gray@amazon.co.uk']



def valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$'
    valid = re.search(regex, email)

    if valid:
        print('valid email')
    else:
        print('invalid email')

    return valid

email = "mysite.com"
valid_email(email) # 제대로 된 이메일이 아님

email = "mike@korea.co.kr"
valid_email(email) # 제대로 된 이메일

email = "mike@daum.net"
valid_email(email) # 제대로 된 이메일


email = "mike@good"
valid_email(email) # 제대로 된 이메일이 아님


s = '한글이에요. good morning. 안녕하세요'
m = re.findall('[ㄱ-힣]+', s)
print(m) # ['한글이에요', '안녕하세요']