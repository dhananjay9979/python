# n1=input("enter n1 ")
# n2=input("enter n2 ")
# try:
#     print("sum of these two numbers is ",
#           int(n1)+int(n2))
# except Exception as e:
#     print(e)
#
# print("This line is very important")


# a=5
# b=0
#
# try:
#     print(a/b)
# except Exception as e:
#     print("hey you got an error",e)

# a=int(input("enter a number"))
# b=int(input("enter a number"))
#
# try:
#     print("resource open")
#     print(a/b)
#
# except Exception as e:
#     print("hey you got an error",e)
# finally:
#     print('resource closed')


a=int(input("enter a number"))
b=int(input("enter a number"))
k=int(input('ENTER a number for k'))
try:
    print("resource open")
    print(a/b)
    print(k)

except ZeroDivisionError as e:
    print("hey you can not divide a number by zero!",e)

except ValueError as e:
    print('invalid input')
except Exception as e:
    print("something went wrong")
finally:
    print('resource closed')
