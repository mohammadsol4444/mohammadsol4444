a=input("Enter a=")
b=input("Enter b=")
c=input("Enter c=")
temp=0
if(a<b):
    temp=a
    a=b
    b=temp
if(a>c):
    temp=a
    a=c
    c=temp
if(b>c):
    temp=b
    b=c
    c=temp
print("sorted=",a,b,c)
