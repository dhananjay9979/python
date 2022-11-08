# import random
# target,guess=random.randint(1,10),0
# count = 1
# while target!=guess:
#     guess= int(input("guess a number between 1 and 10 :"))
#     if guess < target:
#         print("guess a bigger number")
#         count+=1
#     elif guess > target:
#         print("guess a smaller number")
#         count+=1
# print('Well guessed')
# print("you have taken ",count,"chances")
#











# def div(x,y):
#     return x/y
#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
#
# div1 =smart_div(div)
#
# print(div1(5,10))
# -----------------------------------------

# decorator where function executes at last

# def square(func):
#     def inner(a):
#         return (func(a**2))
#     return inner
#
#
# def cube(func):
#     def inner(a):
#         return func (a**3)
#     return inner
#
# @cube
# @square
# def m1(a):
#     return a*2
#
# print(m1(2))
# -------------------------------------------
# decorator where function executes first
# def triple(func):
#     def inner(a):
#         x=func(a)
#         return x*3
#     return inner
#
# def square(func):
#     def inner(a):
#         x=func(a)
#         return x * x
#     return inner
#
#
# @triple
# @square
# def m1(a):
#     return a*2
#
# print(m1(2))

# ----------------------------------------------------------
#
# def fib (n):
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
#
# a=fib(5)
#
#
#
# for z in a:
#     print(z)


# ---------------------------------------

# def gen(n):
#     for i in range(n):
#         if i%2==0:
#             yield i
#
# a=gen(20)
#
# for x in a:
#     print(x)

# ---------------------------------------------------
#
#
# import time
#
# def exetime(func):
#     def inner(*k,**kw):
#         a=time.time()
#         x=func(*k,*kw)
#         b=time.time()
#         print ("time taken for execution in seconds:",b-a)
#     return inner
# @ exetime
# def m1(n):
#     l = []
#     for i in range (n):
#         l.append(i)
#     return l
#
# m1(10000000)
#
# # -------------------------------
# import math
# # print(math.ceil)
# # help(math)
#
# print(dir(math))

# for i in range (1,6):
#     print(i)
