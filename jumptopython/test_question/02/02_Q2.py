# 자연수 13이 홀수 인지 짝수인지 판별할 수 있는 방법에 대해 말해보자

input = 13

if(input % 2 == 0) :
    print("%d (은)는 짝수입니다." % input)
elif(input % 2 != 0) :
    print("%d (은)는 홀수입니다." % input)
elif(input == 0):
    print("%d 입니다." % input)
else :
    print("숫자형이 아니거나 음수입니다.")