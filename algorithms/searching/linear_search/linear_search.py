"""
    Linear search implementation to find an element in a list
    @datetime:: September 24, 2023 11:16 am (UTC-5)
    @lastModified:: September 26, 2023 5:09 am (UTC-5)
    @author:: jac0der
"""

# define a list of numbers
search_list = [11, 23, 8, 14, 30, 9, 6, 17, 22,
                28, 25, 15, 7, 10, 19]

# number to find within the search list
target = input("Enter number: ")

"""
    Function to check list if target is contained within the list.
    A loop is used along with the in keyword.
    @input:: value entered by user
    @output:: True if target exists within the list, otherwise, False.
"""
def serachList(target, list):

    isExists = False
    int_target = 0
    
    # check for invalid user input by trying to cast string
    # value entered by user
    try:
        int_target = int(target)

    except ValueError:

        print(f"Invald input {target}...\n")
        return False
        
    # iterate over the search list to find the target number
    for item in list:

        if(item == int(target)): # cast target to an integer
            isExists = True
            break; # item found so break
    
    if(isExists):
        print(f"Target {target} is in list\n")
    else:
        print(f"Target {target} is not in list\n")

    return isExists

# Function call
serachList(target, search_list)

"""
An easier  way to check if an item is in a list in python
using the in keyword without a loop

def searchList(list, target):
    
    if int(target) in list:
        print("value in list")
        return True
    else:
        print("value NOT in list")
        return False

searchList(search_list, target)

"""