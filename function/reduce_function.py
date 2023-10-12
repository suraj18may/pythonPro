from functools import *
l=[1,2,3,4,5,6,7,8,9]
l2=reduce(lambda x,y:x+y,l)
print(l2)



l3=reduce(lambda x,y:x+y,range(1,10))
print(l3)