class FourCal :
    def __init__(self,first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result

#a = FourCal()

# setdata를 수행하지 않고 add메서드를 먼저 실행하면 에러가 남. 
# 그런 경우를 대비해 생성자를 구현하여 안전하게 대비
# 생성자랑 객체가 생성될 때 자동으로 호출되는 메서드를 의미
#a.setdata(4,2)

# print ("first : ", a.first)
# print ("second : ", a.second)
# print ("add: " , a.add())

b = FourCal(4,2)
print("b first : " , b.first)
print("b second : " , b.second)


class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result

c= MoreFourCal(4,2)
c.add()

print("c add : " , c.add())

d = MoreFourCal(4,2)
d.pow()

print("d pow: " , d.pow())

class safeFourCal(FourCal) :
    def div(self) :
        if self.second == 0:
            return 0
        else :
            return self.first / self.second

e = safeFourCal(4,0)
print ("e div: " , e.div())

class Family:
    lastname = "김"

print("famail lastname: ",Family.lastname)

f = Family()
print("f lastname: " ,f.lastname)