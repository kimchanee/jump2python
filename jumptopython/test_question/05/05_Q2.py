# 객체변수 value 가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다 음과 같이 동작해야 한다.

# 
# cal.add(50) # 50 더 하 기
# cal.add(60) # 60 더 하 기
# 
# print(cal.value) # 100 출 력


# 단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.

class Calculator:
    def __init__(self):
        self.value = 0 
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        
        self.value += val
        if(self.value > 100) :
            self.value = 100

cal = MaxLimitCalculator() 
cal.add(50) # 50 더 하 기
cal.add(60) # 60 더 하 기

print(cal.value) # 100 출 력

