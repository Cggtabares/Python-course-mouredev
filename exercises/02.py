"""
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
"""'''
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_two * num_one
print(product)
division = num_one/num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

'''
'''
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
'''
radius = 30
pi = 3.141625
area_of_circle = (pi * (radius**2))
print(area_of_circle)

circum_of_circle = (2*pi*radius)
print(circum_of_circle)

radius_2 = int(input("Type an amount for the radius "))
area_of_circle_2 = (pi * (radius_2**2))
print(area_of_circle_2)