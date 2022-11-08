# temp in f=5*temp in c/5+32
# temp in c= (temp in f -32)*5/9


temp=input("enter temprature you want to convert")
degree=int(temp[:-1])
unit=temp[-1]

if unit.upper()=='C':
    result=int(round((9*degree)/5+32))
    unit_result="Farenheit"
elif unit.upper()=='F':
    result= int(round((degree-32)*5/9))
    unit_result="Celsius"
else:
    print("inter a valid temparature value")
    quit()
print(f"the temp in {unit_result} is {result} degrees")