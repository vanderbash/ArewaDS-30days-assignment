numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]

print(filtered_numbers)

"""
2. Flatten the following list of lists of lists to a one dimensional list :

   ```py
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```
"""
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist in list_of_lists for inner_list in sublist for num in inner_list]

print(flattened_list)


"""
3. Using list comprehension create the following list of tuples:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
"""
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(result)


"""
4. Flatten the following list to a new list:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
"""
countries = [[(['Finland', 'FIN', 'Helsinki'])], [(['Sweden', 'SWE','Stockholm'])], [(['Norway', 'NOR', 'Oslo'])]]

flattened_list = [item for sublist in countries for item in sublist]

print(flattened_list)

"""
5. Change the following list to a list of dictionaries:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_of_dicts = [
    {'country': country, 'city': city}
    for sublist in countries
    for country, city in sublist
]

print(list_of_dicts)


"""
6. Change the following list of lists to a list of concatenated strings:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

concatenated_strings = [' - '.join(country) for sublist in countries for country in sublist]

print(concatenated_strings)


# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
[(name[0] + " " + name[1]) for row in names for name in row]

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_function = lambda x, m, b: m*x + b

slope = linear_function(3, 5, 1)  # solve for the slope at x = 3, m = 5, b = 1
y_intercept = linear_function(0, 5, 1)  # solve for the y-intercept at x = 0, m = 5, b = 1

print("Slope:", slope)
print("Y-intercept:", y_intercept)