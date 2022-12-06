# 더하기 기능을 구현한 파이썬 코드

# result = 0

# def add (num) :
#     global result
#     result += num
#     return result

# print (add(3))
# print (add(4))

# 만일 더하기 기능이 2개가 필요하다면?(계산기가 2개가 필요하다면?)

# result1 = 0
# result2 = 0

# def add1(num) :
#     global result1 
#     result1 += num
#     return result1

# def add2(num) :
#     global result2
#     result2 += num
#     return result2

# print (add1(3))
# print (add1(4))
# print (add2(3))
# print (add2(7))

# 클래스를 사용해보자.

class Calculator :
    def __init__(self) :
        self.result = 0
    
    def add(self, num) :
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print (cal1.add(3))
print (cal1.add(4))
print (cal2.add(3))
print (cal2.add(7))