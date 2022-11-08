# def countdown(num):
#     print("start countdown")
#     while (num>0):
#         yield num
#         num-=1
# values=countdown(5)
# for x in values:
#     print(x)
# print(type(values))




#
# import random
# names=['sunny','bunny','chinny','vinny']
# subjects=['python','java','blockchain']
#
# def pgen(npeople):
#     result=[]
#     for i in range(npeople):
#         person={
#                 'id':i,
#                 'name':random.choice(names),
#                 'subjects':random.choice(subjects)
#                 }
#         yield person
#
# people=pgen(10)
# for x in people:
#     print(x)






#
# def topten():
#
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# values = topten()
#
# print(next(values))
# print(next(values))
#
#
# for i in values :
#     print(i)





# def topten():
#     n=1
#     while n<=10:
#         sq=n*n
#         yield sq
#         n+=1
#
# values=topten()
#
# for i in values:
#     print(i)
