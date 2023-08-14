'''
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Type a number for the side"))
side_b = int(input("Type a number for the side"))
side_c = int(input("Type a number for the side"))
perimeter = side_a + side_b + side_c
print(perimeter)


#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("type the length of the triangle"))
width = int(input("type the width of the triangle"))
area = length * width
perimeter  = 2 * (length + width)
print(str(area))
print(str(perimeter))


#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("type the radius"))
pi = 3.14
area = (pi * (radius**2))
circumference = (2 * pi * radius)
print(area)
print(circumference)

'''
import math
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_1 = 0
y_1 = (2 * (x_1) - 2)
x_2 = 1
y_2 = (2 * (x_2) - 2)
slope = ((y_2 - y_1)/(x_2 - x_1))
print(f"The slope is: {slope}")

def get_slope(x1,x2,y1,y2):
    slope_slope = ((y2 - y1)/(x2 - x1))
    return slope_slope

def get_eucl_distance(x1,x2,y1,y2):
    eucl_distance = (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))
    return eucl_distance



print(get_slope(2,6,2,10))
print(get_eucl_distance(2,6,2,10))
print(slope == get_slope(2,6,2,10))

