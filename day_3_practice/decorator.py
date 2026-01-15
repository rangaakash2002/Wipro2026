def mydecorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

@mydecorator
def sayhello():
    print("hello")
sayhello()