import collections
import re
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

# Convert the paragraph to lowercase and split it into words
words = paragraph.lower().split()

# Count the frequency of each word
word_counts = collections.Counter(words)

# Convert the Counter object to a list of tuples
word_counts_list = word_counts.most_common()

# Sort the list by count in descending order
word_counts_list.sort(key=lambda x: x[1], reverse=True)

# Print the list of tuples
print(word_counts_list)



text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract the numbers from the text using regex
numbers = re.findall(r'-?\d+', text)

# Convert the extracted numbers to integers
numbers = [int(num) for num in numbers]

# Sort the numbers in ascending order
sorted_points = sorted(numbers)

# Calculate the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

print("Distance between the furthest particles:", distance)



def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable) is not None

print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False


from collections import Counter

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def most_frequent_words(text, count=3):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(count)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print("Cleaned Text:", cleaned_text)

most_frequent = most_frequent_words(cleaned_text)
print("Three most frequent words:")
for count, word in most_frequent:
    print(f"{word}: {count}")
