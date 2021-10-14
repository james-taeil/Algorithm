from functools import reduce
price = 3
count = 4
sum = reduce(lambda x, y: print(x, 'x', y, 'y'), [1,2,3,4])
print(sum)