# 다음은 “test.txt” 라는 파일에 “Life is too short” 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램 이다.
# f1=open("test.txt",'w')
# f1.write("Life is too short")
# 
# f2=open("test.txt",'r') 
# print(f2.read())

# 이 프로그램은 우리가 예상한 “Life is too short” 라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있 도록 프로그램을 수정해 보자.


f1=open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2=open("test.txt",'r') 
line = f2.readline()
print(line)
f2.close()