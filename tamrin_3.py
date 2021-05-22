n=int(input("Enter n="))
a=1
b=1
c=0
i=1
while(i<=n):
    if(i==1):
        print(a)
    elif(i==2):
        print(b)
    else:
        c=a+b
        print(c)
        a=b
        b=c
    i=i+1  
         
