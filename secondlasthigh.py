# a=[10,20,30,60,78,67]
# b=0
# c=0
# for i in a:
#     if i>b: b,c=i,b
#     elif b>i>c:
#         c=i
# print(c)


num_list = [23,11,25,67,76,10]
max = num_list[0]
second_max = num_list[0]
for a in num_list:
    if a > max:
        max = a
print('max value is:', max)
for a in num_list:
    if a>second_max and a!=max:
        second_max = a
print('second max is',second_max )