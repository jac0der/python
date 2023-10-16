'''
    Simple calculator to evaluate basic mathematic operations.
    @datetime:: October 16, 2023 9:18 am (UTC-5)
    @author:: jac0der
'''
# import regex module
import re
import numpy as np

print("Jac0der Calculator")
print("Type 'quit' to exit\n")


previous = 0
run = True

def Calculate():
    # access global variables within local scope of function Calculate()
    global run
    global previous

    # initialize equation to empty string
    equation = ""

    # first calculation attempt
    if previous == 0:

        equation =  input("Enter equation:")

    else:
        equation = input('~ ' + str(previous) + ' ')


    if equation == 'quit':

        print("Goodbye... Have a nice day!")
        run = False

    else:
        # removing letters and special characters from user input
        equation = re.sub('[a-bd-zA-Z,.:()" "]', '', equation)

        if previous == 0:

            previous = eval(equation)

        else:

            previous = eval(str(previous) + equation)

# loop to control the continous running of the calculator
# by using the boolean variable run.
while run:
    Calculate()