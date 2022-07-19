
from operator import add

y = [10, 5, 7, 25, 33] 
z = [2, 10, 8, 11, 20]


#when len of list are same 
x= [y[i] + z[i] for i in range(len(y))   ]

#using map method map(fun, iter)
w =  list(map(add, y, z))

print(w)
print(x)