# Day 3: 30 days of python programming

my_age= 36
my_height= 1.80
comp= 3+6j 

# Script one 
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input('Enter base: '))
h = float(input('Enter height: '))
area = 0.5 * b * h
print('The area of the triangle is:',area)

# Script two
# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
perimeter = a+b+c

print('The perimeter of the triangle is:',perimeter)

# Script three 
# Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter
# (perimeter = 2 x (length + width))

length = float(input('Enter length of rectangle: '))
breadth = float(input('Enter breadth of rectangle: '))
area = length * breadth
print('The area of the rectangle is ',area,' square meters')

# Get the radius of a circle using prompt
# Calculate the area (area = pi * r * r) and circumference (c = 2 * pi * r) where pi = 3.14
import math
r = float(input('Input the radius of the circle: ')) 
area = math.pi * r ** 2 
perimeter = 2 * math.pi * r 
print('The area of the circle is: ',area,' and ','the perimeter is: ',perimeter)

# Calculate the slope, x-intercept and y-intercept of y = 2x-2
# The slope is 2 (coefficient of x) and does not need to be calculated
# x-intercept is the value of x when y=0
# y-intercept is the value of y when x=0
y = 2 * 0 - 2
x = (2 * 0) / 2 
print('The x-intercept of y = 2x-2 is: ',x,' and ','the y-intercept is: ',y)

# Slope is (m = y2-y2 / x2-x1)
# Find the slope and Euclidian distance between point (2, 2) and point (6, 10)
import math
x1,y1,x2,y2 = 2,2,6,10
m = (y2-y1) / (x2-x1)
# Euclidian distance, d = square root of squared distances
d2 = ((y2-y1) ** 2) + ((x2-x1) ** 2)
d = math.sqrt(d2)
print('The slope is: ',m,' and the Euclidian distance is:',d)

# Compare the slopes in task 8 and 9
# The slope for task 8 is 2 and for task 9 is 4
# Using code, i'll lest the slope for task 8 be m0 since that for task 9 is m
m0 = 2
m = 4 
print('Equal: ',m0==m,'Unequal: ',m0 !=m)
# Checking which is greater or less
print('Greater than: ', m0 > m, 'Less than: ', m0 < m)

# Calculate the value of y(y = x^2 + 6x + 9)
# Try to use different x values and figure out at what x value is y going to be 0.
# Using the input function, i tried different values and reduced the value until i got -3
x = int(input('Value of x: '))
y = x ** 2 + 6 * x + 9
print('Value of y: ',y)

# Find the length of 'python' and 'dragon' and make a false comparison statement.
print('Lenght of python: ',len('python'), 'length of dragon: ',len('dragon'))
print('Definetely false: ',len('python')> len('dragon'))

# Use 'and' operator to check if "on" is found in both 'python' and 'dragon'
print('Checking for "on" in "python":', "on" in 'python')

# I hope this course is not full of jargons. Use in operator to check if jargon is in the sentence.
print("jargon in sentence: ", 'jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python: ", 'on' not in ('dragon' and 'python'))


# Find the length of the text python and convert the value to float and convert it to string
a = len('python')
b = float(a)
c = str(a)
print("Length, float and string: ",a,b,c)

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or odd using python?
# Using the modulos operator, which gives the remainders, e.g. x%2 == 0 will be true if x is even and false if x is odd
x = 5
print("x is even: ", x%2==0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print("Checking: ", 7 // 3 == 2.7) # definitely not

# Check if type of '10' is equal to type of 10
print("Cheking again!: ", type('10')== type(10)) # Not equal


# Check if float('9.8') is equal to 10
print("Checking yet again: ", float('9.8') == 10) # it raised a ValueError: invalid literal for float() with base 10: '9.8'

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
x = float(input("Enter hours per week: "))
y = float(input("Enter rate per hour: "))
z = x * y
print("Your weekly earning is: ", z)


# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60 # 365 days, 24 hours, 60 minutes, 60 seconds
print("You have lived for ",seconds, " seconds.")

# Displaying the table
print("1 1 1 1 1")
for i in range(2, 6):
    powers = [i ** j for j in range(4)]
    print(f"{i} {' '.join(map(str, powers))}")