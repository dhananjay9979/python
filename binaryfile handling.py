f=open("lion.jpg",'rb')
f1=open('mypic.JPG','wb')

for i in f:
    f1.write(i)

f1.close()