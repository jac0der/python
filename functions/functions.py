'''
    functions are a way of letting me define certain things that I want to do
    over and over. So if I know that I have something I am going to do a lot
    in the code, write a function for it.

    THEN, instead of having to write this piece of code over and over and over
    again, I can just call the function.

    Thus, A function is a block of code that performs a specific task.
    
    @datetime:: August 17, 2024 4:00 pm (UTC-5)
    @author:: jac0der
'''
from math import sqrt

#*** 1 => Defining a function structure
# indent body of function to make those actions apart of the function body.
# once indentation is removed, that code is no longer a part of the function body.
def FunctionName(Input):
    action
    return Output




#*** 2 => Creating a function
def print_events():
    '''
        function to print even numbers from 2 to 100.
    '''
    for num in range(2, 101, 2):
        print(num)




#*** 3 => Invoke/Call a function.
'''
    After a function is created, it must be invoked/called for the actions defined
    in the function to be executed.
    To invoke/call a function simply use the function name.
'''
print_events()
print()




#*** 4 => Function Parameters and Arguments
'''
    Functions can also accept parameters to be used for processing within its function code body.
'''
numerics = list(range(1, 1000))

# define an empty list
evens = list()

def find_evens(numeric_values):
    ''' 
        function to determine which values are even numbers from a list of integer values.
        numeric_values is the function parameter, specifying that the function accepts 1
        argument when invoked.
    '''
    for i in numeric_values:
        if i % 2 == 0:
            evens.append(i) # add even number to evens list.

# call find_evens function with 1 argument (numerics).
find_evens(numerics)

# print resulting list of even numbers.
print(evens)
print()

'''
    I can also have multiple parameters within a function declaration.
'''
# define 2 sets to be used as arguments to the get_intersection function.
set_a = {2, 8, 9, 4}
set_b = {7, 4, 1, 8}

def get_intersection(set_a, set_b):
    '''
        function which accepts 2 Set parameters and returns the 
        intersection of the two sets.
    '''
    return set_a.intersection(set_b)

#  call/invoke get_intersection function, passing in the two set arguments.
get_intersection(set_a, set_b)

# printing resulting intersecting values.
print(get_intersection(set_a, set_b))




#*** 5 => Assigning function return values to variables.
value = 16
def get_square_root(value):
    return sqrt(value)

square_root = get_square_root(value)

print(square_root)
print()




#*** 6 => Default/Optional Arguments
value = 25

def get_root(value, get_root = True):
    '''
        function to return root of value argument if
        optional boolean value is passed in = True, or not passed in, otherwise
        just return back the value argument.
    '''
    if(get_root):
        
        return sqrt(value)

    else:
        return value

# call get_rrot function without default value specified
print(get_root(value))          # 5.0

print(get_root(value, True))    # 5.0
print(get_root(value, False))    # 25
print()



#*** 7 => Keyword Arguments

# use with default values
def print_welcome_message(name="someone", age="unknown"):
    '''
        function to print a message based on inputs provided,
        otherwise use the default values.
    '''

    print("Hello {}, you are {} years old!".format(name, age))
    
# use default values
print_welcome_message() # Hello someone, you are unknown years old!

# call function specifying which argument should be specified first
print_welcome_message(age=34, name="Paul")
print()


# use with no default values
def print_welcome(name, age):
    print(f"Hello {name}, you are {age} years old.")

# call function specifying order of arguments
print_welcome(age = 34, name = "Peter")
# call function as normal
print_welcome("Jude", 37)
print()










