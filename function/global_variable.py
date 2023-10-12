# a=10
# def test():
#     print(a)
#
# def test1():
#     print(a)
#
# test()
# test1()
# # .......................................................
# a=20
# def test():
#     a=40
#     print(a)
#
# def test1():
#     print(a)
#
# test()
# test1()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def test():
#     global a
#     a=500
#     print(a)
#
# def test1():
#     print(a)
#
# test()
# test1()

# .......................................................................
# a=500
# def test():
#     a=600
#     print(a)
#     print(globals()['a'])
# test()
# recursive function>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(0))
print(factorial(4))
print(factorial(5))
