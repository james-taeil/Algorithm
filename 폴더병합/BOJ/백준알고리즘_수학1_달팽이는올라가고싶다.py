A, B, V = map(int, input().split())

if V == A:
    day = 1
day_up = A - B
day = (V-A)//day_up
if (V-A) % day_up == 0:
    day += 1
else:
    day += 2
print(day)