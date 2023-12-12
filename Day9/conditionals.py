# Day 9: 30 days of python programming

# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 

# Get user input for age
age = int(input("Enter your age: "))

# Check age and provide feedback
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - age
    print(f"You need {years_to_wait} more {'years' if years_to_wait > 1 else 'year'} to learn to drive.")

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:

# Enter your age: 30
# You are 5 years older than me.

# Get user input for my_age
my_age = int(input("Enter your age: "))

# Define your_age (you can modify this variable according to your age)
your_age = 31

# Compare ages and provide feedback
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"You are {age_difference} year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are of the same age.")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. 
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

# Get user input for two numbers
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

# Compare the two numbers and provide feedback
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

### Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# Get the student's score from user input
score = int(input("Enter the student's score: "))

# Assign grades based on the score range
if score >= 80 and score <= 100:
    grade = 'A'
elif score >= 70 and score < 80:
    grade = 'B'
elif score >= 60 and score < 70:
    grade = 'C'
elif score >= 50 and score < 60:
    grade = 'D'
elif score >= 0 and score < 50:
    grade = 'F'
else:
    grade = 'Invalid Score'

# Display the grade
print(f"The student's grade is: {grade}")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

# Get user input for the month
month = input("Enter the name of the month: ")

# Convert the input to lowercase for easier comparison
month = month.lower()

# Determine the season based on the month input
if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Not a valid month'

# Display the determined season
print(f"The season for {month.capitalize()} is {season}.")

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit = 'Grapes'
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else: 
    print('The fruit already exists in the list')


### Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Umar',
    'last_name': 'Aliyu',
    'age': 32,
    'country': 'Nigeria',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '70001'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
# Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
# If a person skills has only JavaScript and React, 
# print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if 'Node' and 'MongoDB' in person['skills']:
        if 'React' in person['skills']:
            print('He is a fullstack developer')
        elif 'Python' in person['skills']:
            print('He is a backend developer')
    elif 'JavaScript' and 'React' in person['skills']:
        print('He is a frondend developer')
    else: 
        print('Unknown title')
             


# If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
first_name = person['first_name']
last_name = person['last_name']
country = person['country']

if person['is_married']==True and person['country']=='Finland':
    print(f'{first_name} {last_name} lives in {country}. He is married.')