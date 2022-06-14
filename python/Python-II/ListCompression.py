

a = [i*i for i in range(5)]

print(a)

#list comprehension
matrix =[
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]
        ]

flatList = [num for row in matrix for num in row]
print(flatList)
