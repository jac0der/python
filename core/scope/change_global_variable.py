''' 
How to change value for a global variable.

@datetime:: February 25, 2025 10:35 pm (UTC-5)
@author:: jac0der
'''

'''
It is not recommended to modify global variables within functions directly.
'''
name = "Natty"


def get_entity():
    # use global keyword to access global variable name to change its value
    global name

    name = "Jwall"
    print(name)

get_entity() # Jwall
print(name)  # Jwall