# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수 is_odd를 작성 해보자.

def is_odd(input):

    if(input < 0) :
        print("자연수를 입력해주세요.")
        return
        
    if(input %2 == 0):
        print("%d (은)는 짝수 입니다." %input)
    else:
        print("%d (은)는 홀수 입니다" %input)


is_odd(4)
is_odd(33)
is_odd(-2)