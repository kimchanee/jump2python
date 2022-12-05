# 다음과 같은 딕셔너리 a 가 있다.
a = dict()
# >>>  a
# {}

# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해보자. 

# 1. a['name'] = 'python'
#a['name'] = 'python'

# 2. a[('a',)] = 'python'
#a[('a',)] = 'python'

# 3. a[[1]] = 'python'
# key 값에 리스트는 쓸 수 없다. 튜플은 key로 사용 가능하다. 
#a[[1]] = 'python'

# 4. a[250] = 'python'
a[250] = 'python'

print("a: " , a)