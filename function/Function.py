# class A():
#     def test(self,name,age):
#         return name,age
#
# re=A()
# print(re.test("Mrinal",10))
# print(type(re.test("Mrinal",10)))
#
# # ..............................................
# def test1():
#     print(10,"mrinal")
#     print(10,"Mohit")
# test1()

# >..............................................
# def test(name):
#     print("hello",name)
#
# test("Mrinal")
# test("amit")

# ...................................................
# def test(number):
#     print("square of ",number,"is",number*number)
#
# test(4)
# test(5)

# ...................................................
# def test(x,y):
#     return x+y,x*y
# res=test(10,20)
# print(res)

# ...................................................
# def test():
#     print("Hello")
# test()
# print(test())

# find even or odd  ....................................................
# def even_or_odd(num):
#     if num%2==0:
#         print("even_number")
#     else:
#         print("odd_number")
# even_or_odd(10)
# even_or_odd(15)

# factorial number............................................
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     print(result)
# fact(5)

# factorial number............................................
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     print(result)
# for i in range(1,5):
#     fact(i)

# return multipul value..........................................
def test(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
x,y,z,z1=test(10,20)
print(x)
print(y)
print(z)
print(z1)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def test(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=test(40,20)
for i in t:
    print(i)

