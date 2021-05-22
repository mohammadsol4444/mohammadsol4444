import math
pi=math.pi
radius=float(input("Enter the radius of the cylinder="))
height=float(input("Enter the height of the cylinder="))
Area=(2*pi*radius*height)+(2*pi*(radius)**2)
volume=pi*height*(radius)**2
print("Area=",Area)
print("volume=",volume)
