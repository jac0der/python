'''
    Exploring string manipulations in python.

    @datetime:: October 04, 2024 10:28 pm (UTC-5)
    @author:: jac0der
'''


#*** 1 => creating a string using both double and single quotes
country = "Barain"
city = 'Barcelonia'
print(country, city, sep=' ', end='\n\n')


#*** 2 => concatenation (using the + operator)
print(country + " " + city)


#*** 3 =>  lower case
title = "The Great Commission"
print(title.lower())


#*** 4 => upper case
print(title.upper())


#*** 5 =>  trimming
language = '   Cobalt      '
print(language)

# trim both sides
print(language.strip())

# trim left side
print(language.lstrip())

# print right side
print(language.rstrip())