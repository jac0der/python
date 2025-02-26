''' 
Explore local scope in Python.

@datetime:: February 25, 2025 10:35 pm (UTC-5)
@author:: jac0der
'''

'''
Local scope exists within functions. A variable declared
within a function is only accessible within that function,
because it has Local Scope - local to the function definition.
'''

def get_entity():
    name = "Jwall"
    print(name)

get_entity()

print(name)  # NameError - 'name' is not defined


def game():
    # drink function is local to game function
    # it can only be called from within the game() function.
    def drink():
        print("coffee")


    drink()

game()
drink() # NameError: name 'drink' is not defined.