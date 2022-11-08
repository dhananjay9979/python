# l=[19, 15, 5, 3, 5, 5, 2]
#
#
# def nlist(l):
#     a=l.count(19)
#     v=l.count(5)
#     if a==2 and v>=3:
#         return True
#     return False
#
# print(nlist(l))


# --------------------------------------------------
#
# l=[19, 19, 15, 5, 5, 5, 1, 2]
#
# def m1(l):
#     n=len(l)
#     m=l.count(l[4])
#     if n==8 and m>2:
#         return True
#     return False
#
# print(m1(l))

# ------------------------------------------------------

# def m1(n):
#     if n>4**4 and n%34==4:
#         return True
#     return False
#
# print(m1(922))

# ------------------------------------

# def m1(n):
#     l=[n]
#
#     for x in range (n-1):
#         l.append(n+2)
#         n=n+2
#     print(l)
#
# m1(4)

# -------------------------------------------------
# checking every nth element is substr of i+1 th element

# l=['a', 'abb', 'sabb']
# def m1(l):
#     l1=[]
#     for i in range(len(l)):
#         if l[i-1] in l[i] and len(l[i-1])!= len(l[i]):
#             l1.append(1)
#         else:
#             l1.append(0)
#         if 0 in l:
#             return True
#         return False
#
# print(m1(l))

# ---------------------------------------------------

# l=[x for x in range(0,1000,)]
# l1=[]
#
# def m1(l):
#     for i in range(len(l)):
#         if abs(l[i+1]-l[i])<=10:
#             l1.append (1)
#         else:
#             l1.append(0)
#
#         if 0 not in l1:
#             return True
#         return False
#
# print(m1(l))

# ------------------------------------------

# l=[1,1,2,1,1,2,-1]
# def m1(l):
#     sum=0
#     for x in l:
#         sum=sum+x
#     if sum==len(l):
#         return True
#     return False
# print(m1(l))

# -----------------------------------------
# s='W3resource Python, Exercises.'
#
# l=s.split()
#
# print(l)
#
# def test(s):
#     import re
#     merged = re.split(r"([ ,]+)", s)
#     return [merged[::2], merged[1::2]]
#
# print(test(s))

# -------------------------------------------------------

# def test(combined):
#    ls = []
#    s2 = ""
#    for s in combined.replace(' ', ''):
#        s2 += s
#        if s2.count("(") == s2.count(")"):
#            ls.append(s2)
#            s2 = ""
#    return ls


# s='( ()) ((()()())) (()) ()'
# l=[]
# s2=''
# # a= s.replace(' ','')
# #
# # print(a)
#
# for x in s.replace(' ','') :
#     s2 += x
# # print(s2)
#
#     if s2.count('(')==s2.count(')'):
#         l.append(s2)
#         s2=''
#
# print(l)


s='( ()) ((()()())) (()) ()'

l=(s.replace(' ','')).split()

print(l)

l=['( ()) ((()()())) (()) ()']