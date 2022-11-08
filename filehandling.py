# syntax open(filename,mode)

# #for reading a file
# f=open('Mydata','r') # to open the file in read mode
#
# print(f.read()) # to read the data from
# print(f.readline(),end='') # to read a specific line
# print(f.readline(5)) # to read only specific characters

# for writing a file
# f1=open('abc','w') # to open the file in write mode
# if the file is not present it will create a new file

# f1.write("something") # for writing data in file
# f1.write(" people")
# f1=open("abc",'a') # first open in append mode and then write
# f1.write(" mobile")
# f1.write('laptop')

##copying data from one file to another file

with open('Mydata','w+') as f: # data to be copied from


    f.write("dhananajay")

    with open("pqr.txt","w") as f1:
        f1.write(d)


# f.close()



# f1=open("abc",'a')
#
# for data in f:
#     f1.write(data)

# f2=open("abc2",'w') # data to be copied to(over write)
# for data in f:
#     f2.write(data)
#
# f.close()
# f2 .close()
