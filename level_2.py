def solution1(n):
  str = ''
  for i in range(n):
      str += '박' if i%2 == 1 else '수'
  return str
# return ('수박'*n) [:n] 입력 받은 만큼 반복, 자릿수 만큼만 slicing

def solution2(arr1,arr2):
   # sum = 0
   # for i in range(len(arr1)):
   #    sum += arr1[i] * arr2[i]
   # return sum
   return sum(map(lambda x: x[0] * x[1], zip(arr1,arr2)))

def solution3(left,right):
   answer = 0
   for num in range(left,right+1):
      print(num)
      cnt = 0
      for i in range(1,num+1):
         if num%i == 0:
            cnt += 1
      answer = answer + num if cnt%2 == 0 else answer - num
   return answer  
 
def solution4(s):
   return ''.join(sorted(s,reverse=True))

def solution5(price, money, count, result):
   total = 0
   # price * c for c in range(count)
   for c in range(count):
      print(c)
      total += price * (c+1)
   return abs(money-total) if money < total else 0

def solution6(s):
   return len(s) in [4,6] and s.isdigit()

def solution7(arr1,arr2):
   for i in range(len(arr1)):
      for j in range(len(arr1[i])):
         print(arr1)
         arr1[i][j] += arr2[i][j]
   return arr1

# print(solution7([[1,2],[2,3]],[[3,4],[5,6]]))
# print(solution7([[1],[2]],[[3],[4]]))
# [[4,6],[7,9]]

def solution8(n,m):
   return(m *(n * '*' + '\n'))

def solution9(n,m):
   a = min(n,m)
   b = max(n,m)
   print(a,b)
   q = b//a
   # r = m%n
   # while r > 0:
   #    print(a, b)
   #    b = m%n
   #    a = m//n
   # return [a,b, '']   
   # return [(n if m%n == 0 else 1),(m if m%n == 0 else n*m)]

def solution10(n):
   reverse_base = ''
   while n > 0:
      reverse_base += str(n%3)
      n = int(n//3)
   return int(reverse_base,3)

print(solution9(3,12))