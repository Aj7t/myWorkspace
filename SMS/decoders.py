
import logging 
import time

def dividee(func):
    def inner(a, b):
        if b == 0:
            logging.error(f' raised an error when divided by zero at '+ " "+  time.strftime("%H:%M:%S", time.localtime()))
            return None

        return func(a, b)
    return inner


@dividee
def divide(a, b):
    print(a/b)

divide(7, 0)