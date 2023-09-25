"""
    Linear search implementation to fin an element in a list
    @datetime:: September 24, 2023 11:16 am (UTC-5)
    @author:: jac0der
"""

# define a list of numbers
search_list = [11, 23, 8, 14, 30, 9, 6, 17, 22,
                28, 25, 15, 7, 10, 19]

# number to find within the search list
target = input("Enter number: ")

# iterate over the search list to find the target number
for value in search_list:

    if(value == int(target)):
        print("value in list")
        break


"""
An easier  way to check if an item is in a list in python
using the in keyword

def searchList(list, target):
    
    if int(target) in list:
        print("value in list")
        return True
    else:
        print("value NOT in list")
        return False

searchList(search_list, target)

"""