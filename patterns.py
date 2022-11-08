# square
# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()
#increasing triangle
# n=5
# for i in range(n):
#     for j in range(i):
#         print('*',end=" ")
#
#     print()
#decreasing triangle
# n=5
# for i in range(n):
#     for j in range(n-i,0,-1):
#         print('*',end=" ")
#     print()
#decresing triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=" ")
#     print()

# left sided triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

#right sided triangle
# n=5
# for i in range(n):
#     for j in range(i):
#         print(' ',end=" ")
#     for j in range(i,n):
#         print('*',end=" ")
#     print()
#hill pattern
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# reverse hill
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i+1,n):
#         print("*",end=" ")
#     print()
#  diamond pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(1,n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()
#diamond with no space
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(1, n):
#     for j in range(i + 1):
#         print(" ", end="")
#     for j in range(i, n):
#         print("*", end="")
#     for j in range(i, n - 1):
#         print("*", end="")
#     print()
#void diamond in sqare
n=int(input("enter number of rows: "))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()