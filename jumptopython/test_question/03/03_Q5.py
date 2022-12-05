# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for 문을 사용하여 A 학급의 평균 점수를 구해보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

counter = len(score)
totalScore = 0

for sc in score :
    totalScore = totalScore + sc

avg = totalScore / counter

print("A 학급의 평균점수는 %0.1f 점 입니다." %avg)
