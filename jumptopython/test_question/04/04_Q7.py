# 다음과 같은 내용을 지닌 파일 test.txt 가 있다. 이 파일의 내용 중 “java” 라는 문자열을 “python” 으로 바꾸어서 저장해 보자.
# Life is too short 
# you need java
# replace 함수를 사용해 보자.

f = open("test_Q7.txt","r")

while True :
    text = f.readline()

    text.replace("java","python")
    
    if not text :
        break

    print (text)

f.close()

# for line in f.readlines() :
#     line=line.strip()
#     print(line)
# f.close()