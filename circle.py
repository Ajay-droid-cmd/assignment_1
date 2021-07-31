''' a) Write a Python program to calculate surface volume and area of a sphere
     b) Write a Python program to calculate arc length of an angle. '''
import math
print("Surface volume& area of a sphere")
x=float (input("Enter the radius of the sphere"))
a=4*math.pi*x*x
v=4/3*math.pi*x*x*x 
print("\nSurface volume = %2f"%a)
print("\nArea of sphere = %2f"%v)


# Write a Python program to calculate arc length of an angle

print("\n arc length ")
def arclength(d,a):
    if a>=360 :
        print("Angle cannot be formed")
        return 0
    else:
        arc=(math.pi*d)*(a/360.0)
        return arc

d=float(input("Enter the diameter"))
a= float(input("Enter the angle"))
arclen = arclength(d,a)
print(arclen)
