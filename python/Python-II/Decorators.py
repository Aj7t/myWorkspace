'''
 to modify the behaviour of a function or class
'''


def outer_fun(func):
    def inner_fun():
        print("Before calling the function")
        func()
        print("After calling the function")
    return inner_fun


@outer_fun
def ajit():
    print("This is a function")
    
    
# myfun= outer_fun(func)
# outer_fun(func) is equivalent to @outer_fun
# func = outer_fun(func)
ajit()


#prequisite for decorators

# def add():
#     print("adding")

# add()

# def remove(add):
#     print("removing")