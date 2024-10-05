'''
    Exploring python's input function to get user input
    into programs.

    @datetime:: October 04, 2024 10:52 pm (UTC-5)
    @author:: jac0der
'''

#*** 1 => syntax
# input("User prompt ")


#*** 2 => accept and store a user input to a variable
name = input("What is your name?\n")

print(f'Your name is {name}')


#*** 3 => casting an input to be used in a math operation
age = int(input("What is your age?\n"))
additional_age = int(input("Enter a number to add to your age.\n"))

print(f"Your new age is {age + additional_age}")