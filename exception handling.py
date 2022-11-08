# printing exception information
#
# try:
#     print(10/0)
# except Exception as msg:
#     print("exception raised and it's description is: ",msg)


# try with multiple except blocks
# import sys
# while True:
#     try:
#         a=float(input("enter 1st number"))
#         b=float(input("enter 1st number"))
#         print(a/b)
#     except ZeroDivisionError as e :
#         print(e,"error occured so dividing by 1")
#         b=1
#         print(a / b)
#
#     except ValueError as e:
#         print('value error occured: ',e)
#         print( exit())
#
#
#
#     except TypeError as e:
#         print("value error occured: ",e,"enter integer or decimal point numbers")

    # finally:
    #     print(a * b)


# raise exceptions
# def simple_interest(amount, year, rate):
#     try:
#         if rate > 100:
#             raise ValueError(rate)
#         interest = (amount * year * rate) / 100
#         print('The Simple Interest is', interest)
#         return interest
#     except ValueError:
#         print('interest rate is out of range', rate)
#
#
# simple_interest(800, 6, 8)
#
# simple_interest(800, 6, 800)


# single except block can handle multiple exceptions
#
# try:
#     a = float(input("enter 1st number"))
#     b = float(input("enter 1st number"))
#     print(a/b)
#
#
# except (ZeroDivisionError, ValueError) as e:
#     print("enter valid numbers, the problem is :", e)



# default exception block must be last


# try:
#     a = float(input("enter 1st number"))
#     b = float(input("enter 1st number"))
#     print(a / b)
# except:
#     print("default except block")
#
# except (ZeroDivisionError, ValueError) as e:
#     print("enter valid numbers, the problem is :", e)









#
# s='dhananjay'
# s1=''
# for x in s:
#     s1=s1+hex(ord(x))
#
# print(s1)

# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
#
# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
#
# age = int(input("enter your age"))
#
# if age > 60:
#     raise TooOldException("your age already crossed marriage age no chance of getting married")
# elif age < 18:
#     raise TooYoungException("Please wait some more time you will definitely get perfect match")
# else:
#     print("thanks for registration.........you will get match details by mail")




c5a=int(input('enter number of 5rs coin available :'))
c1a=int(input('enter number of 1rs coin available :'))
amount=int(input("enter price of item : "))
ab=(c5a*5) +(c1a*1)
c5=int(amount//5)
c1=int(amount%5)

if ab>=amount and c5a>=c5 and c1a>=c1:
    print(f"you can buy the item by paying {c5} '5rs' coins and {c1} '1rs' coin")

elif ab>=amount and c5a>=c5 and c1a<c1:
    print(c1-c1a," '1rs' coin needed, you have sufficient money but not change")

elif ab>=amount and c5a<c5 and c1a>=c1:
    print(c5-c5a," '5rs' coin needed, you have sufficient money but not change")

elif ab < amount :
    print(" insufficient funds")
