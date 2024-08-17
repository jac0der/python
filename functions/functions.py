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




















