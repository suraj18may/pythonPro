def outer():
    print("outer function")
    def inner():
        print("inner function")
    print("outer function calling inner function")
    inner()
outer()

# a function can return another function

def outer():
    print("outer function")
    def inner():
        print("inner function")
    print("outer function calling inner function")
    return inner

f1=outer()
f1()
f1()


