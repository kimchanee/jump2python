# 홍길동씨의 주민등록번호는 881120-1068234 이다. 
# 홍길동씨의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자
# (문자열 슬라이싱 기법을 사용해보자)

res_num = "881120-1068234"

print("YYYYMMDD : %s" % res_num[0:6])
print("back_num : %s" % res_num[7:])

# 배열을 이용할 수도 있음
#arr = res_num.split("-")
#print("YYYYMMDD : %s" % arr[0])
#print("back_num : %s" % arr[1])
