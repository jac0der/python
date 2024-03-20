'''
    A dictionary is an ordered collection of key-value pairs.
    Each key is connected to a value by a colon (:),
    and I can use a key to access the value associated with that key.

    A dictionary is used to represent/connect related pieces of data for objects.
    such as: List of words and their meanings
             List of people names and their favorite numbers
             List of mountains and their elevations etc...
    
    @datetime:: October 13, 2023 11:49 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => Creating a dictionary

jamaican_culture = {
    'bird': 'doctor bird',
    'fruit': 'ackee',
    'dish': 'ackee and saltfish',
    'tree': 'blue mahoe',
    'mountain': 'blue mountain',
    'river': "dunn's river",
    'reggae': 'bob marley',
    'sports': 'usain bolt'
}
print(jamaican_culture)

student_average = {
    'phil': 55,
    'sarah': 70,
    'edward': 65,
    'jen': 95
}
print(student_average, '\n')

# create empty dictionary
empty_dict = {}
empty_dict2 = dict()


#*** 2 => Add a new key-value pair
jamaican_culture['hero'] = 'marcus garvey'

student_average['esther'] = 98
student_average['ruby'] = 49

print(jamaican_culture)
print(student_average, '\n')


#*** 3 => Access a value in a dictionary - use the key
# get esther's average score
print(f"Esther's average is:: {student_average['esther']}")

# get the national bird of jamaica
print(f"Jamaica's national bird is the '{jamaican_culture['bird'].title()}'", '\n')


student_average.get('ruby', 'invalid key...')

#*** 4 => Modifying values in a dictionary - assign new value to existing key
# change sarah's grade
student_average['sarah'] = 75 
print(student_average, '\n')



#*** 5 => Dynamically building a dictionary
# define an empty dictionary
people_languages = {}

people_languages['esther'] = 'hebrew'
people_languages['sarah'] = 'greek'
people_languages['phil'] = 'spanish'
people_languages['jen'] = 'english'
people_languages['edward'] = 'dutch'
people_languages['dill'] = 'spanish'
print(people_languages)


#*** 6 => removing key-value pairs - use del keyword
del people_languages['edward']
print(people_languages, '\n')

# removing jen itme from the dictionary
# pop returns the value of the item popped.
people_languages.pop('jen')

# but using popitem, the actual key: value pair is popped.
people_languages.popitem()


#*** 7 => using get() method to access a key
# use get() method to prevent error when accessing a key which 
# doesn't exists

# phil exists
print(people_languages.get('phil').title())

# jane is not a key in dictionary - so returns None
print(people_languages.get('jane'))
print('\n')

# specify optional error message to be returned instead of None
print(people_languages.get('jane', 'Invalid key entered'))


#*** 8 => Looping through a dictionary
# loop all key, value in a dictionary.
# person => key; language => valuue
for person, language in people_languages.items():
    print(f"{person.title()} language is {language.title()}")

print('\n')


#*** 9 => Looping through a dictionary keys
# loop student average dictionary
for key in student_average.keys():
    print(f"{key.title()} received an average score!")

print('\n')


#*** 10 => Looping through a SORTED dictionary keys
# loop SORTED student average dictionary
# use sorted keyword to temporarily sort the dictionary's
# keys List.
for key in sorted(student_average.keys()):
    print(f"{key.title()} received an average score!")



print('\n')
#*** 11 => check if a value exists in a dictionary (key or value)
# define a list of languages
search_name = 'erwin'
search_language = 'spanish'

if search_name not in people_languages.keys():
    print(f"{search_name.title()} is not in the List of people and the languages they speak")


if search_language in people_languages.values():
    print(f"{search_language.title()} is in the List of people and the languages they speak")
print('\n')


#*** 12 => Looping through a dictionary values
# loop student average dictionary
for score in student_average.values():
    print(f"{score}")

print('\n')


'''
    A Set is a collection in which each item must be unique.
'''

#*** 12 => looping unique values in a List (from dictionary keys() or values())
# Use a Set to store unique values, so convert List with duplicated values 
# to a Set. using set() converts the dictionary's values list to a Set of
# uniuque languages.
for language in set(people_languages.values()):
    print(language)

print('\n')


#*** 13 => Define a Set manually
# duplicated python will be removed - only keeping 1 instance of python
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
print('\n')

#*** 14 => Add items to a Set
languages.add('rust')
languages.add('golang')
print(languages)
print('\n')

#*** 15 => Remove items from a Set - 3 ways of removing an item from a Set
languages.remove('c')
languages.discard('ruby')
languages.pop()

print(languages)


#*** 16 => Clear/emptying a Set
languages.clear()
print(languages)



#*** 17 => Nesting Dictionaries within a List

# define an empty List to store aliens
aliens = []

# create 30 aliens to store in List - use range method
for count in range(30):

    #creating a mnew alien on each iteration of loop
    new_alien = {'color': 'red', 'speed': 'slow', 'points': 5}

    # append/add new alien to the List
    aliens.append(new_alien)


# print first 5 aliens
for alien in aliens[:5]:
    print(alien)

print('\n')

print(f"Total alien count is: {len(aliens)}")

# modify the first 3 aliens in the List
for alien in aliens[:3]:

    if(alien['color'] == 'red'):
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


print(aliens)
print('\n')


#*** 18 => Nesting List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['extra-cheese', 'green-peppers', 'peperoni']
}

print(f"You have ordered the {pizza['crust'].title()}-crust pizza.")

for topping in pizza['toppings']:
    print(topping)

print('\n')

#*** 19 => Nesting Dictionary in a Dictionary
# values of the dictionary keys are values themselves.
users = {
    'jdoe': {
        'first': 'jane',
        'last': 'doe',
        'location': 'ethiopia'
    },
    'phil': {
        'first': 'phil',
        'last': 'burges',
        'location': 'egypt'
    },
    'sarah': {
        'first': 'sarah',
        'last': 'nuten',
        'location': 'israel'
    }
}

print(users)

for username, userinfo in users.items():
    print(f"Username: {username}")
    print(f"\t Fullname: {userinfo['first']} {userinfo['last']}")
    print(f"\t Location: {userinfo['location']}")


#*** 20 => Find length of a dictionary
# use len() method to find length of a dictionary
fruit_colors = dict()
fruit_colors['grape'] = 'purple'
fruit_colors['water melon'] = 'red'

print(len(fruit_colors))



#*** 21 => dictionary membership test - use in operator
print('grape' in fruit_colors)  # True


#*** 22 => dictionary comprehension
'''
    Dictionary comprehension is an elegant and concise way
    to create dictionaries in python.

    Create a dictionary that maps the values of a list of
    numbers to their squares.
'''
numerics = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in numerics}
print(square_dict)


# Construct a new dictionary with new prices by increasing the 
# prices by 50% for those that are more than $2.

old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}
new_price = {key: value * 1.5 if value > 2 else value for (key, value) in old_price.items()}
print(new_price)


