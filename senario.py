f=open(r"C:\Users\ADMIN\Desktop\data.txt",'r')
a=f.readlines()
l=[]
for x in a:
    l.append(x.split(","))
for x in l:
    if int(x[2])>35:
        print(x)

