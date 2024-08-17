'''
    functions are a way of letting me define certain things that I want to do
    over and over. So if I know that I have something I am going to do a lot
    in the code, write a function for it.

    THEN, instead of having to write this piece of code over and over and over
    again, I can just call the function.

    A function is a block of code that performs a specific task.
    
    @datetime:: August 17, 2024 4:00 pm (UTC-5)
    @author:: jac0der
'''


#*** 1 => Defining a function structure
# indent body of function to make those actions apart of the function body.
# once indentation is removed, that code is no longer a part of the function body.
def FunctionName(Input):
    action
    return Output


#*** 2 => Creating a function
def print_events():

    for num in range(2, 101, 2):
        print(num)


#*** 3 => Call a function.
'''
    After a function is created, it must be invoked for the actions defined
    in the function to be executed.
    To invoke/call a function simply use the function name.
'''
print_events()
print()


#*** 4 => Function Parameters and Arguments
'''
    Functions can also accept arguments to be used for processing within its function code body.
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

# call find_evens function with 1 argument.
find_evens(numerics)
print(evens)
print()


# define 2 sets to be used as arguments to the get_intersection function.
set_a = {2, 8, 9, 4}
set_b = {7, 4, 1, 8}

def get_intersection(set_a, set_b):
    '''
        function which accepts 2 Set parameters and returns the 
        intersection of the two sets. 
    '''
    return set_a.intersection(set_b)

#  call/invoke get_intersection function
get_intersection(set_a, set_b)

print(get_intersection(set_a, set_b))















