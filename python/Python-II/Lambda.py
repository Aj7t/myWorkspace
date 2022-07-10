
# lambda argument(s): expression

#Normal python function
def myFun(x):
    return 5+x

print(myFun(2))


#Lambda function
y = lambda x: x + 10
print(y(5))



# Program to filter out only the even items from a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: (x%2 == 0) , list1))

print(new_list)
