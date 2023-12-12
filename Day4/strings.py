# Day 4: 30 days of python programming

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print(' '.join(['Thirty','Days','Of','Python']))

# Concatenate the string 'Coding', 'For' , 'All' into a single string, 'Coding For All'
print(' '.join(['Coding','For','All']))

# Declare a variable named company and assign it to the initial value "Coding For All"
company = 'Coding For All'
# Print the variable company using print().
print(company)

# Print the length of the string "company" using len() method and print()
string = 'company'
length = len(string)
print(length)

# Change all the characters to uppercase letters using upper() method
print(string.upper())

# Change all the characters to lowercase letters using lower() method
print(string.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(string.capitalize())

# for swapcase()
string.swapcase()

# for title
string.title()

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods
print('Using .index(): ', company.index('Coding')) 
print('Using .rindex(): ', company.rindex('Coding')) 
print('Using .find(): ',company.find('Coding')) 

# Replace the word coding in the string 'Coding For All' to Python
print('Coding for all'.replace('Coding','Python'))
print(company.replace('Coding','Python'))

# Change Python for Everyone to Python for All using the replace method or other methods
print('Python for everyone'.replace('everyone','all'))

# Split the string 'Coding For All' using space as the separator (split()) 
print('Coding For All'.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# What is the character at index 0 in the string Coding For All ?
print('Coding For All'[0])   
print(company[0]) 

# What is the last index of the string Coding For All? 
print('Coding For All'[-1]) 
print(company[-1])  

# What character is at index 10 in "Coding For All" string ?
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'
sentence = 'Python For Everyone'
words = sentence.split()
acronym = ''
for word in words:
    print(word[0], end='.')
# prints P.F.E

# Create an acronym or an abbreviation for the name 'Coding For All'
sentence = 'Coding For All'
words = sentence.split()
acronym = ''
for word in words:
    print(word[0], end='.')
# prints C.F.A

# Use index to determine the position of the first occurrence of C in Coding For All
print(sentence.index('C')) #0

# Use index to determine the position of the first occurrence of F in Coding For All.
print(sentence.index('F')) #7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l')) #19

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because')) #31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because')) #47

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:47 + len('because')])

# Does ''Coding For All' start with a substring Coding?
cfa = 'Coding for All'
print(cfa.startswith('Coding')) # True

# Does 'Coding For All' end with a substring coding?
print(cfa.endswith('coding'))   # False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '  
print(string.rstrip())

# Which one of the following variables return True when we use the method isidentifier():
## 30DaysOfPython
## thirty_days_of_python
print('30DaysOfPython: ','30DaysOfPython'.isidentifier()) # False 
print('thirty_days_of_python: ','thirty_days_of_python'.isidentifier()) # True


# The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '# '.join(libraries)
print(joined_libraries)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines:
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square 

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')