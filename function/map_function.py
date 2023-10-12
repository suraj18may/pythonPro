def double(x):
    return 2*x
l=[1,2,3,4,5]
l1=list(map(double,l))
print(l1)
# .......use lambda function/...................
l=[1,2,3,4,5,6]
l1=list(map(lambda x:2*x,l))
print(l1)