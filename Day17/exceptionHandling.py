"""
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
"""
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack the first five countries
*nordic_countries, es, ru = names

print("Nordic Countries:", nordic_countries)
print(f'es: {es}, ru: {ru}')