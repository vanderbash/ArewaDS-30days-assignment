# Day 5: 30 days of python programming
# Declare an empty list
list_1 = list()
list_2 = []
print(f' the two lists are {list_1},{list_2}')

# Declare a list with more than 5 items
top = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# Find the length of your list
list_length = len(top)
print(f'The length of the list is {list_length}') 

# Get the first item, the middle item and the last item of the list
first_item =  top[0] # Monday
middle_item =  top[int(len(top)/2)] #
last_item =  top[-1]  # 
print(f'The first, middle and last items in the list are {first_item},{middle_item} and {last_item} respectively ')

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Bashir', 35, 1.73,'Married','Jigawa']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)
print(mixed_data_types)

# Print the number of companies in the list
comp_length = len(it_companies)
print(len(mixed_data_types))
print(f'The number of companies in the list is {comp_length} ')

# Print the first, middle and last company
first_comp = it_companies[0] # first : Facebook
middle_comp = it_companies[len(it_companies)//2] # middle: Apple
last_comp = it_companies[-1] # last: Amazon
print(f'The first middle and last companies are {first_comp},{middle_comp} and {last_comp} respectively.')
# Print the list after modifying one of the companies
it_companies[0] = 'Blackberry' 
print(it_companies)

# Add an IT company to it_companies
it_companies.insert(0,'Google')  # adding Google back at position one
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'Zipline')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
'#;  '.join(it_companies)

# Check if a certain company exists in the it_companies list.
'Facebook' in it_companies # False

# Sort the list using sort() method
it_companies.sort() # method returns none
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse() # also returns none
print(it_companies)

# Slice out the first 3 companies from the list
it_companies[:3]

# Slice out the last 3 companies from the list
it_companies[-3:]

# Slice out the middle IT company or companies from the list
it_companies[len(it_companies)//2:len(it_companies)//2+1]

# Remove the first IT company from the list
it_companies.pop(0)
it_companies

# Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()
it_companies

# Destroy the IT companies list
del it_companies


# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)
# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy() # front_end contains the two lists
# first find the index of redux
full_stack.index('Redux') # 4
full_stack.insert(5,'Python') # insertion is done before the index
full_stack.insert(full_stack.index('Python')+1,'SQL')
full_stack 

# The following is a list of 10 students ages:
ages = [29, 22, 19, 28, 20, 30, 26, 19, 26, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)  
min_age = min(ages)  # 19
max_age = max(ages)  # 26
print(f'The minimum age is {min_age} and the maximum age is {max_age} ')
# Add the min age and the max age again to the list
ages.extend([20,30])
ages

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages_length = len(ages)
len(ages) # 12
print(ages[int(len(ages)/2-1)],ages[int(len(ages)/2)]) # 24,24

if ages_length % 2 == 0:
  cond_1 = ages[ages_length//2]
  cond_2 = ages[ages_length//2-1]
  median_age = (cond_1 + cond_2)/2

else: 
  median_age = ages[ages_length//2]
print(f'The median age of the ages is {median_age}')

# Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages) # 22.75
print(f'The average age is {average}')
# Find the range of the ages (max minus min)
rng = max(ages) - min(ages) # 7
print(f'The range of the ages is {rng}')
# Compare the value of (min - average) and (max - average), use abs() method 
abs(min(ages) - average) == abs(max(ages)- average) # False

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries.sort()
countries_length = len(countries)

if countries_length % 2 == 0:
  cond_1 = countries[countries_length//2]
  cond_2 = countries[countries_length//2-1]
  middle_country = (cond_1 , cond_2)

else: 
  middle_country = countries[countries_length//2]
print(f'The mid country in the countries list is {middle_country}')

mid_country = countries[len(countries)//2]
print(f'The middle country in the list is {mid_country} ') # Lesotho

# confirming with index
countries.index('Lesotho') # index is 96 : correct. Lesotho is in the 97th position out of the 193 countries.

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries_first_three = countries[0 : 3]
scandic_countries = countries[3:]
print(countries_first_three)
print(scandic_countries)


print(f'The length of the two halves are {countries_first_three} and {scandic_countries}')


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
CH,RU,US,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic
print(f'The scandic countries in the last list given are {scandic}')