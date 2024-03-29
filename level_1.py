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

def solution6(absolutes,signs):
   answer = 0
   for i in range(len(absolutes)):
      if signs[i]: 
         answer += absolutes[i]
      else:
         answer -= absolutes[i]   
   return answer

def solution7(phone_number):
  answer = ''
  for i in range(len(phone_number)):
    print(i, phone_number[i])
    answer += '*' if i < len(phone_number)-4 else phone_number[i] 
  return answer    

def solution8(numbers):
   print(sum(numbers))
   return sum(range(10)) - sum(numbers)

def solution9(arr):
  if len(arr) > 1:
    arr.remove(min(arr))
    return arr
  else:
    return -1
  
def solution10(s):
   lenth = len(s)/2
   # 2.5 => 3
   # 2 => 2, 3
   return s[int(lenth)] if lenth%1 == 0.5 else s[int(lenth)-1:int(lenth)+1]  

print(solution10("abcde"))
print(solution10("qwer"))

# 반복문 축약형
a_list = [1,3,2,5,1,2]
b_list = [a*2 for a in a_list]
print(b_list)

