# 1. Explain the difference between map, filter, and reduce.
"""
map: The map function applies a given function to each element in an iterable and returns an iterator of the results. It transforms each element based on the provided function and returns an iterator with the transformed values.
filter: The filter function applies a given predicate function to each element in an iterable and returns an iterator containing only the elements for which the predicate function returns True. It filters out unwanted elements from the iterable.
reduce: The reduce function is available in the functools module in Python. It takes a binary function (a function that takes two arguments) and an iterable, and it applies the function cumulatively to the elements of the iterable to reduce them to a single value. It returns the final accumulated result.
"""

"""
2. Explain the difference between higher order function, closure and decorator
Higher-Order Functions: In Python, functions are first-class citizens, which means they can be treated as objects and passed as arguments to other functions or returned as values from functions. A higher-order function is a function that takes one or more functions as arguments or returns a function as its result. It operates on functions just like any other data type. Higher-order functions enable powerful functional programming techniques and allow for code that is more modular and reusable.
Closures: A closure is a function object that remembers values in the enclosing lexical scope even if they are not present in memory. In simple terms, a closure is a function that retains access to variables from its outer (enclosing) scope even after the outer function has finished executing. It "closes over" those variables and can access and modify them. This is particularly useful for creating data privacy and maintaining state between function calls.
Decorators: A decorator is a special kind of function that can modify the behavior of other functions or classes without changing their source code directly. Decorators are denoted by the @ symbol in Python and are applied to functions or classes directly above their definitions. They provide a way to add functionality to existing functions or classes by wrapping them with additional code. This can be useful for aspects such as logging, timing, authorization, or modifying the return values of functions.


"""

# 3. Define a call function before map, filter or reduce, see examples.
def call(func, *args):
    return func(*args)

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = call(map, square, numbers)
# squared is a map object: [1, 4, 9, 16, 25]

def call(func, *args):
    return func(*args)

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = call(filter, is_even, numbers)
# evens is a filter object: [2, 4, 6, 8, 10]

from functools import reduce

def call(func, *args):
    return func(*args)

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = call(reduce, multiply, numbers)
# product is 120

#  Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for country in countries:
    print(country)

    # Use for to print each name in the names list.
for name in names:
    print(name)


  # Use for to print each number in the numbers list.
for number in numbers:
    print(number)


    
# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries)

#  Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)



# Use map to change each name to uppercase in the names list
uppercase_names = list(map(str.upper, names))
print(uppercase_names)



#  Use filter to filter out countries containing 'land'.
filtered_countries = list(filter(lambda country: 'land' not in country.lower(), countries))
print(filtered_countries)


# Use filter to filter out countries having exactly six characters.
filtered_countries = list(filter(lambda country: len(country) == 6, countries))
print(filtered_countries)


# Use filter to filter out countries containing six letters and more in the country list.
filtered_countries = list(filter(lambda country: len(country) >= 6, countries))
print(filtered_countries)


# Use filter to filter out countries starting with an 'E'
filtered_countries = list(filter(lambda country: country.startswith('E'), countries))
print(filtered_countries)




# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

result = (
    reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
)

print(result)



# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

my_list = [1, "Meet", 2.5, "Them", True, "Here"]
string_list = get_string_lists(my_list)
print(string_list)


# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

sum_total = reduce(lambda x, y: x + y, numbers)
print(sum_total)




# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]

sentence = reduce(lambda x, y: x + ", " + y, countries)
sentence = sentence + " are north European countries."

print(sentence)


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


"""
Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
"""
def categorize_countries(country_list, pattern):
    return [country for country in country_list if pattern in country]

# ountries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
pattern = "land"

matching_countries = categorize_countries(countries, pattern)
print(matching_countries)


#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_starting_letter(country_list):
    country_dict = {}
    for country in country_list:
        starting_letter = country[0]
        if starting_letter in country_dict:
            country_dict[starting_letter] += 1
        else:
            country_dict[starting_letter] = 1
    return country_dict

# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
country_counts = count_countries_by_starting_letter(countries)
print(country_counts)


# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(country_list):
    return country_list[:10]
# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Germany", "France", "Italy", "Spain", "Portugal"]
first_ten_countries = get_first_ten_countries(countries)
print(first_ten_countries)


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list):
    return country_list[-10:]
# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Germany", "France", "Italy", "Spain", "Portugal"]
last_ten_countries = get_last_ten_countries(countries)
print(last_ten_countries)
