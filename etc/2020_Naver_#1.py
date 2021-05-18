m = "acbbcdc"
k = "abc"
x = ''

# for i in k:
#     a = m.find(i)
#
#     if

    # x += str(a)
    # if (x[0] > x[1]) or (x[1] > x[2]) or x[0] > x[2]:
    #     a = m.find(i, 2)
    #     x += str(a)
    #     print(x)

# for
#     k_str = m[:a]
#     k_str2 = m[a+1:]
#     m = k_str + k_str2


a = m.find(k[0])
b = m.find(k[1])
c = m.find(k[2], 2)

print(a)
print(b)
print(c)

if (a <= b) or (b <= c):
    k_str = m[:a]
    k_str2 = m[a+1:]
    m = k_str + k_str2

    k_str3 = m[:b]
    k_str4 = m[b + 1:]
    m1 = k_str3 + k_str4

    k_str5 = m[:c]
    k_str6 = m[c + 1:]
    m2 = k_str5 + k_str6

print(m)
print(m1)
print(m2)

# 2번 문제에 대한 공지입니다.
# 제한사항에서 a는 왼쪽에서 몇 번째 블록인지를 나타내는데,
# 이때 0번째부터 셉니다. 즉, 가장 왼쪽의 블록이 0번째 블록입니다.







