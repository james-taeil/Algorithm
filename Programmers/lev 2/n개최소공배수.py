def solution (arr):
  answer = 1
  for el in arr:
    answer = lcm(answer, el)
  return int(answer)

def gcd(num1, num2):
  if (num1 == 0):
    return num2
  return gcd(num2 % num1, num1)

def lcm(num1, num2):
  return (num1 * num2) / gcd(num1, num2)

arr = [2,6,8,14]
print(solution(arr))