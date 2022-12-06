# 리스트 중에서 홀수에만 2를 곱하여 저장한느 다음 코드가 있다.
#  numbers=[1,2,3,4,5] 
#  result=[]
# for n in numbers:
#   if n % 2 == 1:
#       result.append(n*2)
#
# 위 코드를 리스트 커프리헨션(list comprehension)을 사용하여 표현해보자.

numbers=[1,2,3,4,5] 
result=[]

result = [num * 2 for num in numbers if num % 2 != 0]

print ("result : %s" %result)