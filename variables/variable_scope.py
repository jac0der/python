'''
    Exploring variable scope in python.
    A variable scope specifies the region where I can access a variable.

    Python has 3 variable scopes:
        1. local        (local variables)
        2. global       (global variables)
        3. nonlocal     (nonlocal variables)

    @datetime:: August 18, 2024 4:24 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => global variables (global scope)
''' 
    a global variable is a variable defined outside of a function, thus have
    global scope.
    declare global variables, accessible inside or outside of a function.
'''
fruit = 'apple'
fav_language = 'python'

def get_fruit():
    print(f'local: {fruit}')    

get_fruit()                 # apple
print(f'global: {fruit}')   # apple
print()



'''
    updating a global variable value within a function, creates
    a new local variable within the function, thus resulting in different values.
'''
def get_fav_language():
    fav_language = 'rust'
    print(f'local: {fav_language}')

# print updated local instance of fav_language
get_fav_language()                                  # rust

# print unchanged value of fav_language
print(f'global: {fav_language}')                    # python
print()



'''
    to change the global value within a local scope, use the 'global'
    keyword.
    TRY AVOIDING USE OF global KEYWORD...
'''
def change_fav_language():
    global fav_language
    fav_language = 'go'
    print(f'local: {fav_language}')

# print updated global instance of fav_language
change_fav_language()                               # go

# print updated value of fav_language
print(f'global: {fav_language}')                    # go
print()




#*** 2 => local variables (local scope)
'''
    variables defined within a function is local only to that function,
    thus cannot be accessed outside the function.
'''
def which_os():
    # local variable with local scope
    os = "Linux GNU"

    print(os)

which_os()  # Linux GNU

# try access os variable outside of function
print(os) # error




