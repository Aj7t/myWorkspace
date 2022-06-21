
def star(func):
    def inner(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)
    return inner


def atSign(func):
    def inner(*args, **kwargs):
        print("@" * 20)
        func(*args, **kwargs)
        print("@" * 20)
    return inner


@atSign
@star
def fun():
    print(" Thank you for decorating me")


fun()