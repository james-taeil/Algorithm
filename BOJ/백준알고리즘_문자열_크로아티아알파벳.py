str_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
print(s, 's')
for i in str_list:
    print(i, 'i')
    s = s.replace(i, 'a')
    print(s, 's')
print(len(s))


# ljes=njak
# ddz=z=
# nljj
# c=c=
