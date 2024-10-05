'''
    Exploring how to get the type of a variable
    in python

    @datetime:: October 04, 2024 11:12 pm (UTC-5)
    @author:: jac0der
'''

#*** 1 => type() function determines type of a variable
age = 20
cost = 200.58
number = 1 + 2j

print(f'Type of age is {type(age)}')
print(f'Type of cost is {type(cost)}')
print(f'Type of number is {type(number)}')

'''
    Type of age is <class 'int'>
    Type of cost is <class 'float'>
    Type of number is <class 'complex'>
'''