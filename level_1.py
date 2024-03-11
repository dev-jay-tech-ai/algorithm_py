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

def solution4(seoul):
   return "김서방은 " + str(seoul.index('Kim')) + "에 있다"

def solution5(arr,divisor):
   result = list(filter(lambda n:n%divisor == 0,arr))
   return sorted(result) if len(result) > 0 else [-1]

print(solution5([3,2,6],10))