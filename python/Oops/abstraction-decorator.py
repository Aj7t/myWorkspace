class decorator_class:
    def __init__(self, func):
     self.func = func

    def __call__(self, ):
       product = args[0] * args[1]
       print("Product of {} and {} is {} ".format(args[0], args[1], product))
       return self.func(args[0], args[1])


@decorator_class
def add(num1, num2):
   value = num1 + num2
   print("The sum of {} and {} is {}.".format(num1, num2, value))


# execute
add(10, 20)









# class animalClass:
#     def __init__(self, func):
#         self.func = func
        
#     def countLegs(self, *args):
#         product = args[0] * args[1]
#         print("Total legs is {} ".format(product))
#         countHand()
#         return self.func(args[0], args[1])


# @animalClass
# def countHand(num1, num2):
#    res = num1 + num2
#    print("Total hands is {} .".format(res))


# # execute
# countHand= animalClass(countHand(2, 2))
