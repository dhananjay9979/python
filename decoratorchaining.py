def doubledecor(func):
    print("1")
    def inner():
        print("2")
        x=func()
        print("3")
        return 2*x
    return inner

def squaredecor(func):
    print("4")
    def inner():
        print("5")

        x=func()
        print("6")
        return x*x
    return inner

@doubledecor
@squaredecor

def num():
    print("7")
    return 10

print(num())



# changing sequence of decorators
# def doubledecor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
#
# def squaredecor(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
#
# @squaredecor
# @doubledecor
#
# def num():
#     return 10
# print(num())

