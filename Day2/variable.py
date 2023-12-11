#Day 2: 30 Days of python programming
#Exercise level 1
firstname = "Bashir"
lastname = "Iliyasu"
middlename = "Bashir"
fullname = "Bashir Iliyasu Bashir"
countryName = "Nigeria"
cityName = "Kano"
age = 36
year = 2023
is_married = True
is_true = False
is_light = True
a, b, c = 2, 3, 4

#Exercise level 2
print(type(firstname))
type(lastname)
type(fullname)
type(middlename)
type(countryName)
type(cityName)
print(type(age))
type(year)
type(is_married)
type(is_true)
print(type(is_light))

print(len(firstname))
print(len(lastname))
print(len(middlename))
compare = len(firstname)>len(lastname)>(middlename)
print(compare)

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_two * num_one
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one**num_two
print(exp)

import math
dir(math)
floor_division = math.floor(division)
print(floor_division)

radius = 30
area_of_circle = math.pi * radius * radius
circum_of_circle = 2 * math.pi * radius

print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius * radius
print("Area of the circle:", area_of_circle)

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
middlename = input("Enter your middlename: ")
countryName = input("Enter your country name: ")
age = input("Enter your age name: ")
print(firstname)
print(lastname)
print(middlename)
print(countryName)
print(age)