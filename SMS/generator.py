x = [1, 2, 3, 4, 55, 6, 7,8, 20]  

#generator func 
def myGen():
    for i in range(len(x)):
        yield x[i]


a = myGen()


# a = ( i for i in x)
 
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
