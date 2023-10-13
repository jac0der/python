'''
    A dictionary is a collection of key-value pairs.
    Each key is connected to a value by a colon (:),
    and I can use a key to access the value associated with that key.

    A dictionary is used to represent/connect related pieces of data for objects.
    such as: List of words and their meanings
             List of people names and their favorite numbers
             List of mountains and their elevations etc...
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
print(f"Jamaica's national bird is the '{jamaican_culture['bird'].title()}'")




















