'''
    List is an ordered collection of similar or different types of 
    items separated by commas and enclosed within brackets []
    
    @datetime:: March 20, 2024 6:42 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => Creating a List

jamaica = ['ackee', 'saltfish', 'jelly', 'jerked chicken']
print(jamaica)

empty_list = list()
empty_list2 = []
print(empty_list, empty_list2)

# I have five students in a class and I want to group all of their test 
# scores together
scores = [70, 85, 67.5, 90, 80]
print(scores)



#*** 2 => Accessing List Items - via index
# Each element has a specific number/index
# first element has index 0, 2nd element has index 1, 3rd element has index 2 etc...

print(jamaica[1]) # access the 2nd element - using index 1
print(scores[4]) # access the 5th (last) element - using index 4



#*** 3 => Accessing List Items - via negative indexing (access elements in reverse order)

print('access 2nd to last element: ', jamaica[-2]) # print 2nd to last item in list
print('access last element', scores[-1])  # access the 5th (last) element - using index -1

# gives an error as there is no 6th last element
# trying to access something that is not in my list
# print(scores[-6])
# OR as well
# print(scores[5]) there is no index five so list index out of range error occurs

 
#*** 4 => Accessing List Items - via slicing
# The format for list slicing is [start:stop:step]

# jamaica = ['ackee', 'saltfish', 'jelly', 'jerked chicken']
print(jamaica[::2]) # ['ackee', 'jelly'] step up by 2
print(jamaica[1:4]) # ['saltfish', 'jelly', 'jerked chicken']


# scores = [70, 85, 67.5, 90, 80] - original list
# pick out the 1st and 2nd element from the list
# start at 0 (zero), then go up to but not including (:), 2 (not including index 2)
print(scores[0:2])   # [70, 85]
























