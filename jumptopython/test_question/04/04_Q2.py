# 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성해보자. (단,입력으로 들어오는 수의 개수는 정해 져 있지 않다.)
# 평균 값을 구할 때 len 함수를 사용해보자


def cal_input(*args) :

    result = 0

    for i in args :
        result = result + i

    avg = result / len(args)

    print("평균:  " , avg)

cal_input(1,2)
cal_input(5,6,7)