import math
v=float(input("Enter the wind speed="))
t=float(input("Enter the tempreture="))
h=10
wind_chill=13.12+0.6215*t-11.37*math.pow(v,0.16)+0.3956*t*math.pow(v,0.16)
print("the wind chill index=",wind_chill)
