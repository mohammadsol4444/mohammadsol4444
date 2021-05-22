ans=str(input("Do you want to continue="))
if(ans=="YES" or ans=="yes"):
    n=int(input("Enter n="))
    j=0
    a=[]
    for i in range(1,int(n/2)):
        if(n%i==0):
           a[j]=i
           j+=1
    sum=a[0]
    for i in range(1,j):
        sum+=a[j]
else:
    print("finished")
