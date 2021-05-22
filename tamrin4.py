from math import tan,pi
length=float(input("Enter the length of the sides="))
n=int(input("Enter the number of sides="))
Area=(n*(length)**2)/(4+tan(pi/n))
print("Area=",Area)
