by=int(input("Enter th birth year="))
bm=int(input("Enter the birth month="))
bd=int(input("Enter the birth day="))
ny=int(input("Enter the current year="))
nm=int(input("Enter the current month="))
nd=int(input("Enter the current day="))
if(nd<bd):
    bm-=1
    nd+=30
if(nm<bm):
    ny-=1
    nm+=12
month=nm-bm
year=ny-by
day=nd-bd
days=day+month*30+year*36
print("life(year)="+str(year))
print("life(month)="+str(month))
print("life(day)="+str(day))
print("life(hour)="+str(days*24))
print("life(minute)="+str(day*24*60))
print("life(seconds)="+str(day*24*60*60))
