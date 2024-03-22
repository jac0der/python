'''
    List is an ordered collection of similar or different types of 
    items separated by commas and enclosed within brackets []
    
    @datetime:: March 20, 2024 6:42 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => creating a list

jamaica = ['ackee', 'saltfish', 'jelly', 'jerked chicken']
print(jamaica)

empty_list = list()
empty_list2 = []
print(empty_list, empty_list2)

# I have five students in a class and I want to group all of their test 
# scores together
scores = [70, 85, 67.5, 90, 80]
print(scores)



#*** 2 => accessing list items - via index
# Each element has a specific number/index
# first element has index 0, 2nd element has index 1, 3rd element has index 2 etc...

print(jamaica[1]) # access the 2nd element - using index 1
print(scores[4]) # access the 5th (last) element - using index 4



#*** 3 => accessing list items - via negative indexing (access elements in reverse order)

print('access 2nd to last element: ', jamaica[-2]) # print 2nd to last item in list
print('access last element', scores[-1])  # access the 5th (last) element - using index -1

# gives an error as there is no 6th last element
# trying to access something that is not in my list
# print(scores[-6])
# OR as well
# print(scores[5]) there is no index five so list index out of range error occurs

 
#*** 4 => accessing list items - via slicing
# The format for list slicing is [start:stop:step]

# jamaica = ['ackee', 'saltfish', 'jelly', 'jerked chicken']
print(jamaica[::2]) # ['ackee', 'jelly'] step up by 2
print(jamaica[1:4]) # ['saltfish', 'jelly', 'jerked chicken']


# scores = [70, 85, 67.5, 90, 80] - original list
# pick out the 1st and 2nd element from the list
# start at 0 (zero), then go up to but not including (:), 2 (not including index 2)
print(scores[0:2])   # [70, 85]


# start somewhere in list and go all the way to the ending value
# just remove end index value
print(scores[1:])   # # [85, 67.5, 90, 80]
print(scores[2:])   # # [67.5, 90, 80]



#*** 5 => add elements to a list (insert, append, extend)
jamaica.insert(1, 'blue mountain coffee')
print(jamaica) # ['ackee', 'blue mountain coffee', 'saltfish', 'jelly', 'jerked chicken']

# a student was sick during test and had to take the test later, 
# so add their score to the list too
scores.append(82)  # [75, 85, 67.5, 90, 80, 82]
print(scores)

odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

# adding elements of one list to another
odd_numbers.extend(even_numbers)
print(odd_numbers) # [1, 3, 5, 2, 4, 6]



#*** 6 => changing list elements
# jamaica = ['ackee', 'blue mountain coffee', 'saltfish', 'jelly', 'jerked chicken']
jamaica[4] = 'jerk'
print(jamaica) # ['ackee', 'blue mountain coffee', 'saltfish', 'jelly', 'jerk']


# Scores = [70, 85, 67.5, 90, 80] - original list
# the first studen got 5 extra points so correct score to be 75 instead of 70
scores[0] = 75
print(scores)

scores[2] = [] # assign an empty list to index 2
print(scores)  # [75, 85, [], 90, 80]



#*** 7 => removing items from a list (del, remove('item'), pop(), pop(index))

del jamaica[-1]
print(jamaica)

# use del function to remove an item from a list
places = ['miami', 'homestead', 'orlando', 'disney']
del places[1]

places.remove('disney')
print(places)

# pop removes item at specified index and allows
# me to work with the poped/removed item in code.
# user list.pop(), with no index specified to remove
# last item in list - i can work with popped items.
places.pop()  # return last item
places.pop(0) # return item at index 0
print(places)


#*** 8 => clear a list
tux_commands = ['awk', 'ls', 'chown', 'chmod', 'grep']
tux_commands.clear()
print(tux_commands)



#*** 9 => get list length
print(len(jamaica))



#*** 10 => accessing a list within a list
scores = [75, 85, 67.5, 90, 80] 
# change index 2 to be a list
scores[2] = ["Hello", "World"]
print(scores)   # [75, 85, ['Hello', 'World'], 90, 80]

# access 3rd element (list)/index 2, then access the 2nd element/index 1
print(scores[2][1])  # World



#*** 11 => sorting a list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']



#*** 12 => sorting a list in reverse order permanently
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']



#*** 13 => sorting a list temporarily
books = ['math', 'banking', 'programming', 'accounting']
print(sorted(books))    # ['accounting', 'banking', 'math', 'programming']
print(books)            # ['math', 'banking', 'programming', 'accounting']



#*** 14 => sorting a list in reverse order temporarily
print(sorted(books, reverse=True))



#*** 15 => reversing a list - no sorting, change original order of items
numbers = [9, 3, 5, 7]
print(numbers)         # [9, 3, 5, 7]
numbers.reverse()
print(numbers)         # [7, 5, 3, 9]



#*** 16 => using range() to make a list of numbers
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

# using a loop
numerics = list()
for i in range(0, 21, 2):
    numerics.append(i)

print(numerics) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



#*** 17 => perform simple statistics with a list of numbers
print(min(numerics))
print(max(numerics))
print(sum(numerics))



#*** 18  => Iterate through a list
fruits = list()

fruits.append('apple')
fruits.insert(1, 'orange')
fruits.insert(2, 'banana')

for fruit in fruits:
    print("I really like {}".format(fruit))



#*** 19 => check if item exists in a list or not
vegetables = ['carrot', 'cabbage', 'lettuce']

print('tomato' in vegetables) # False
print('cabbage' in vegetables) # True
print('lettuce' not in vegetables) # False



#*** 20 => Iterate through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli' ]

for player in players[:3]:
    print(player.title())



#*** 21 => Copy a list
# copy a list by slicing an entire existing list by [:],
# ignoring the start and end indicies.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

friend_foods.append('jerk')
print("\nMy friends favorite foods are:")
print(friend_foods)



#*** 22 => list comprehension
 # put first 10 squares in a list
square = [num**2 for num in range(11)]
print(square) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a numbers list with elements in the  
# form of 2 to the power of i, where i takes values from 1 to 5.
twos = [2**i for i in range(1,6)]
print(twos)  # [2, 4, 8, 16, 32]

# create list of even numbers
evens = [num for num in range(11) if num % 2 == 0]
print(evens) # [0, 2, 4, 6, 8, 10]

# find the vowels in the string "Python" using list comprehension
vowels = [l for l in 'Python' if l in ['a', 'e', 'i', 'o', 'u']]
print(vowels)  # ['o']

# find even numbers that are divisible by 5 from 0 to 100.
even = [num for num in range(101) if num % 2 == 0 and num % 5 == 0]
print(even)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print "Even" and "Odd" in a list for even and odd numbers in list
# # [1, 2, 3, 4, 5, 6]
even_odd = ["Even" if i % 2 == 0 else "Odd" for i in [1, 2, 3, 4, 5, 6]]
print(even_odd) # ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']



















