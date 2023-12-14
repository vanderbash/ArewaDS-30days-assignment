# Writ a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

print(generate_random_user_id())  # Output: something like 'e3R9D7'
print(generate_random_user_id())  # Output: something like 'x8Y2aF'


def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    user_ids = []
    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_characters))
        user_ids.append(user_id)

    return user_ids

# generated_ids = user_id_gen_by_user()

#for user_id in generated_ids:
#    print(user_id)

#or 

print(user_id_gen_by_user()) # user input: 5 5


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue


color = rgb_color_gen()
print(color)  # Output: (123, 45, 67) (example RGB values)


"""
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""

def list_of_hexa_colors(num_colors):
    hex_colors = []
    
    for _ in range(num_colors):
        color = ''.join(random.choices('0123456789ABCDEF', k=6))
        hex_colors.append('#' + color)
    
    return hex_colors

colors = list_of_hexa_colors(5)
print(colors)  # Output: ['#1A2F4B', '#FFA0C2', '#8D67E9', '#5B9C0F', '#CDE456']


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.



def list_of_rgb_colors(num_colors):
    rgb_colors = []
    
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        rgb_colors.append(color)
    
    return rgb_colors

colors = list_of_rgb_colors(5)
print(colors)  # Output: [(123, 45, 67), (12, 34, 56), (78, 90, 123), (234, 56, 78), (45, 67, 89)]


def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        # Generate random values for RGB components (0-255)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Append the RGB tuple to the colors list
        colors.append((red, green, blue))
    
    return colors

# Generate a list of 5 RGB colors
num_of_colors = 5
rgb_colors = list_of_rgb_colors(num_of_colors)
print(rgb_colors)


# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(lst):
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    return shuffled_list
my_list = [1, 2, 3, 4, 5]

shuffled = shuffle_list(my_list)
print(shuffled)


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def generate_unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

random_numbers = generate_unique_numbers()
print(random_numbers)