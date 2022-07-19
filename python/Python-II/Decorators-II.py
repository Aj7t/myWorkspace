
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 20)
#         func(*args, **kwargs)
#         print("*" * 20)
#     return inner


# def atSign(func):
#     def inner(*args, **kwargs):
#         print("@" * 20)
#         func(*args, **kwargs)
#         print("@" * 20)
#     return inner


# @atSign
# @star
# def fun():
#     print(" Thank you for decorating me")


# fun()


def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 1)