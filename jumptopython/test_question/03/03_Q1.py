# 다음 코드의 결괏값은 무엇일까?

# 1 a="Lifeistooshort,youneedpython" 
# 2
# 3 if"wife"ina:print("wife")
# 4 elif"python"inaand"you"notina:print("python")
# 5 elif"shirt"notina:print("shirt")
# 6 elif"need"ina:print("need") 7 else:print("none")

a = "Life is too short, you need python" 

# a 안에 wife가 있으면
if "wife" in a: print("wife")
# python이 a 안에 있고, you가 a 안에 없으면
elif "python" in a and "you" not in a: print("python")
# shirt가 a안에 없으면
elif "shirt" not in a: print("shirt")

elif "need" in a: print("need") 

else: print("none")