def solution1(x):
  return x % sum([int(digit) for digit in str(x)]) == 0

def solution2(a, b): 
    return sum(range(min(a,b),max(a,b)+1))

def solution3(num):
  for i in range(500):
     if num == 1:
        return i
     num = num/2 if num % 2 == 0 else num * 3 + 1
  return -1   

print(solution3(1))