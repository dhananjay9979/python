# import array
# array_name=array.array('type code',[elements])
# stu_roll=array.array('i',[101,102,103,104,105])
# from array import *
# array_name = array('type code', [elements])
# stu_roll=array('i',[101,102,103,104,105])

# creating array by user input for loop
# from array import *
# stu_roll=array('i',[])
# n= int(input("enter number of elements: "))
#
# for i in range(n):
#     stu_roll.append(int(input("enter element:")))
#
# for i in range(len(stu_roll)):
#     print(stu_roll[i])
# print(stu_roll)


# creating array by user input while loop
# from array import *
# stu_roll=array('i',[])
# n= int(input("enter number of elements: "))
# i=0
# j=0
# while i<n:
#     stu_roll.append(int(input("enter element:")))
#     i+=1
# while( j<len(stu_roll)):
#     print(stu_roll[j])
#     j+=1
# print(stu_roll)
#
from array import *
stu_roll=array("i",[101,102,103,104,105,106,107])
for i in range(len(stu_roll)):
    print(i,"=",stu_roll[i])
print(stu_roll)
print('------------------------------')
a=stu_roll[1:5]
for i in a:
    print(i)

print(a)

