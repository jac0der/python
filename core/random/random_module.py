'''
    random module is used to generate random numbers
    or to randomly select an item from a sequence.

    @datetime:: September 7, 2025 8:42 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => import random module
import random
# import random as r
# from random import randint


# functions for integers
#*** 2 => generate a random integer
number = random.randint(7,14)
print(number)


#*** 3 => generate random number up to 4
range_number = random.randrange(5)
print(range_number)


#*** 4 => generate random number specifying range (and step)
print(random.randrange(20, 40))
print(random.randrange(60, 80, 2))


print()

#*** 5 => return a random element from a non-empty sequence
fruits = ['apple', 'grape', 'orange', 'banana', 'strawberry', 'blueberry', 'melon', 'apple']
print(random.choice(fruits))


# return a random letter from a string
country = 'Cuba'
print(random.choice(country))



#*** 6 => shuffle or rearrange items in a sequence.
print()
random.shuffle(fruits)
print(fruits)


#*** 7 => 
print(random.sample(fruits, 2))


print()
books = {
    'c++': 'Tour of C++',
    'c#': 'cSharpe for everyone',
    'python': 'Fundamental python'
}
print(books)
print(random.sample(sorted(books), 2))