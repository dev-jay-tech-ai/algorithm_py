def solution1(x):
  return x % sum([int(digit) for digit in str(x)]) == 0

def solution2(a, b): 
    return sum(range(min(a,b),max(a,b)+1))

print(solution2(3,5))