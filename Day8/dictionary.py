# Day 8: 30 days of python programming

# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Wizzy'
dog['color'] = 'Black'
dog['breed'] = 'Dalmatian'
dog['legs'] = 4
dog['age'] = 4

# Create a student dictionary and add first_name, 
# last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student = dict()
student.update({'first_name': 'Bashir', 'last_name': 'Iliyasu','gender': 'male','age': 35,'marital_status': 'Married','skills':['MySQL','PowerBI','Python'], 'country':'Nigeria','city': 'Jigawa','address': 'Taura'})

# Get the length of the student dictionary
print('length of student dict: ', len(student)) # 9
# Get the value of skills and check the data type, it should be a list
student['skills']
print(type(student['skills']))   
# Modify the skills values by adding one or two skills
student['skills'].append('R')
print('Checking the modification:', student)

# Get the dictionary keys as a list
print('dictionary keys as a list: ',student.keys())

# Get the dictionary values as a list
print('dictionary value as a list: ',student.values())
# Change the dictionary to a list of tuples using items() method
print('list of tuples of dict items: ',student.items())
# Delete one of the items in the dictionary
student.pop('address')
student

# Delete one of the dictionaries
del student
print(student) # NameError