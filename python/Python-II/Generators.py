#using function
def squares(x):
    for i in range(x):
        yield i*i

gen = squares(5)
while True:
    try:
        print("Received on next(): ", next(gen))
    except StopIteration:
        break

#Generator Expression
gen = (i*i for i in range(5))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))