
def outer_fun(func):
    def inner_fun():
        print("Before calling the function")
        func()
        print("After calling the function")
    return inner_fun



def func():
    print("This is a function")
    
    
myfun= outer_fun(func)
myfun()


#prequisite for decorators

# def add():
#     print("adding")

# add()

# def remove(add):
#     print("removing")