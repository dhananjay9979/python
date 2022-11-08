# x = 4
# r = x%2
# if r==0:
#     print("even")
#     if x>5:
#      print('greater')
#     else:
#       print("not so great")
#
# else:
#     print("odd")


#
# for i in range(1500,2701):
#     if i % 7==0 and i %5 ==0:
#         print(i)



#
# t=input("enter temperature in degree farenheit or cecius")
#
# if t[-1].lower()== 'f':
#     t1= ((int(t[:-1])-32)*5)/9
#
# elif t[-1].lower()=='c':
#     t1=((int(t[:-1])*9)/5)+32
#
#
# print(t1)




# import random
# r=random.randint(1,9)
# count=1
# while True:
#     g=int(input("enter a number between 1 to 9: "))
#     if g==r:
#         print('right guess')
#         break
#     elif g>r:
#         print("guess lower number ")
#         count+=1
#
#     elif g<r:
#         print("guess higher number")
#         count+=1
# print('attempts',count)




# for i in range(1,5):
#     print('* '* i)
# for i in range(5,0,-1):
#     print("* "* i)

#
# def fib(n):
#     a,b=0,1
#     i=0
#     while a<n:
#         print(a,end=" ")
#         a,b=b,a+b
#         i+=1
#
# fib(50)




# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)


# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
#
# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col
#
# print(multi_list)




import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")






