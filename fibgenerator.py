# def fib(n):
#     a,b=0,1
#     i=0
#     while i<n:
#         yield a
#         a,b=b,a+b
#         i+=1
#
# f=fib(10)
# for x in f:
#     print(f[5])


# generating n fibonacci numbers
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#
#         yield a
#         a,b=b,a+b
#
# f=fib(15)
# for x in f :
#     print(x)


# generating fib till n
# def fib(n):
#     a, b = 0, 1
#
#     for i in range(n):
#         if a<n:
#          yield a
#          a, b = b, a + b
#
#
# f = fib(100)
# for x in f:
#     print(x)

# n=6
# l=[]
# for i in range(1,n):
#     if n%i==0:
#         l.append(i)
# x=sum(l)
#
# if n==x:
#     print("perfect number")
#
# else:
#     print("not")


# n=input('enter a number')
# l=len(n)
# sum=0
# for i in n:
#     sum += int(i)**l
#
# print(sum)
# if sum == int(n):
#     print("armstrong nuber")
# else:
#     print("not")

#
# n=1000
# sum = 0
# l1=[]





# print(l1)

# -----------------------------------------------
# n=1000
# l=[]
# for i in range (2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#
#     else:
#         l.append(i)
#
# print(sum(l))
#
# n2=sum(l)
# l1=[]
# for i in range (1,n2):
#     n1 = str(i)
#     l = len(n1)
#     sum=0
#     for j in n1:
#         sum+=int(j)**l
#     if sum == i:
#         l1.append (i)
# print(l1)
#
# --------------------------------------------------------
# l1=[]
# n=10
# for i in range(2,n+1):
#     l=[]
#     for j in range(2,i):
#         if i%j==0:
#             l.append(j)
#     if len(l)==0:
#         l1.append(i)
# print(l1)
#
#


# l=[1,88,66,58,36,46,99,451,4,6,8,32,7]
# a=0
# for i in l:
#     if i>a:
#         a=i
# print(a)

# for i in range(len(l)-1,0,-1):
#     for j in range(i,len(l)-1):
#         if l[j]>l[j+1]:
#             l[j] ,l[j + 1]=l[j + 1],l[j]
#
# print(l)




# for i in range(len(l)-1,0,-1):
#     for j in range(i,len(l)-1):
#         if l[j]>l[j+1]:
#             l[j] ,l[j + 1]=l[j + 1],l[j]
#
# print(l)



# l=[1,88,66,58,36,46,99,451,4,6,8,32,7]
#
#
# for i in range(len(l)):
#     minpos=i
#     for j in range(i,len(l)):
#         if l[j]< l[minpos]:
#             minpos=j
#
#     l[i],l[minpos]= l[minpos],l[i]
#
#
# print(l)

# for i in range(len(l)):
#     minpos = i
#     for j in range(i, len(l)):
#         if l[j] < l[minpos]:
#             minpos = j
#
#     l[i], l[minpos] = l[minpos], l[i]
#
# l = [ 88, 66, 58, 36,1, 46, 99, 451, 4, 6, 8, 32, 7]
# # for i in range (len(l)):
# #     for j in range(i,len(l)):
# #         if l[j]<l[i]:
# #             l[i],l[j]=l[j],l[i]
# #
# # print(l)
#
# a=l[0]
# for i in range(len(l)):
#     if l[i]<a:
#         a=l[i]
#
# print(a)

#
#
# print('\n'.join
#       ([''.join
#         ([('Engineer'[(x-y)%8 ]
#            if((x * 0.05)**2 + (y * 0.1)**2 - 1)
#                **3 - (x * 0.05)**2 *(y * 0.1)
#                **3 <=0 else' ')
#            for x in range(-30,30)])
#         for y in range(15,-15,-1)]))

# a = 10 if 10>20 else 30 if 40>50 else 60
# print(a)
# a=input()
# b=input()
# def addnum(a:int,b:int) ->int:
#     return(a+b)
#
# print(addnum(a,b))

# print('10\n20\n30',end=' anji ')
#
# s = '

def dec(fun):
    def inner(name):
        if name == 'chu':
            print('Hi',name)
        else:
            fun(name)
    return inner

def dec2(fun):
    def inner(name):
        if name == 'phu':
            print('Hi',name)
        else:
            print('hi',name)
    return inner

@dec2
@dec
def a(name):
    print('I am', name)


a('chu')