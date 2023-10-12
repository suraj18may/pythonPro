# positinal argument>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.....
# def test(name,age):
#     print(name,age)
#
# test("mrinal",10)
#
# def test(a,b):
#     print(a-b)
# test(20,30)
# test(30,20)

# keyword Argument...........................................

# def test(name,age,add):
#     print("my name is",name,"age is",age, "m from ",add)
#
# test(age=29,add="Noida",name="Mrinal")

# default Argument..............................
# def test(name="suraj"):
#     print(name)
# test()
# test("Mrinal")

# def test(name,age,add="Noida"):
#     print(name,add,age)
# test("Mrinal",30)

# variable Argument............................................
# def test(*n):
#     print(n)
# test(10)
# test(10,20)
# test(10,20,30)
# <<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
# def test(*n):
#     result=0
#     for i in n:
#         result=result+i
#     print(result)
# test(10)
# test(10,20)
# test(10,20,30)

# positional and variable argument.............
def test(a,*s):
    print(a)
    for i in s:
        print(i)
test(10)
test(10,20)
test(10,20,30)


