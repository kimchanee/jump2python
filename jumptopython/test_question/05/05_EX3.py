# import mod1

# print("mod1 add: ", mod1.add(3,4))
# print("mod1 sub: ", mod1.sub(4,2))

from mod1 import *

print("add: " , add(3,4))
print("sub: " , sub(4,2))

import mod2 

print("mod2 PI: ",mod2.PI)

a = mod2.Math()

print("a solv: " ,a.solv(2))
print("mod2 add: " , mod2.add(mod2.PI, 4.4))