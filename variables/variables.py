"""
     variables are a way of storing data/information that I may want to 
     keep for later.
     A variable is general a placeholder for a value.
     In python I dont have to tell the computer what type I want my variable 
     to be, It figures the type out automatically.
"""

# Global variables - defined outside the scope of any function
# so I can access them from anywhere.
# so the variables declared below out side a function are all global.

#*** 1 => Creating and assigning variables
# integer variables
one = 1
two = 2
three = 3
four = 4

#*** 2 => use the print() function to print the variable values to the screen
print('one: ', one)
print('two: ', two)
print('three ', three)
two = 4         # over write value of variable two
print('two: ', two)      # now variable two has new value of 4
print('one:', one)      # re-use variable one
print()

#*** 3 => Creating variables of a different type - Decimal and Strings
# decimal/float variable
Decimal = 1.1

# string variable - concatenation
StringVar = "Hello" + "1"


print('Decimal: ', Decimal)
print('StringVar: ', StringVar)



#*** 4 => Creating a Constant (in global scope)
# constant in ALL CAPS
PI = 3.14
print('PI: ', PI)
print()


#*** 5 => Creating local variable within scope of a function
#         these variables are not accessible outside the function
def FunctionName():
    global one  # specify global variable in local scope
    # could also just remove from within function
    # and just access directly print(one) since one is a global variable
    newVar = "World" # local variable newVar, can't access outside function
    print('global variable in function: ', one)
    print('local variable in function: ', newVar)
    return

# call/run function
FunctionName()
# print(newVar) # when active this yields an error as it is not in global scope



#*** 6 => shorthand way/notation of creating a variable
four, five, six = 4, 5, 6 # four = 4; five = 5; six = 6
print()
print('four: ', four)
print('five: ', five)
print('six: ', six)





#*** 7 => create a variable based on the sum of two previous variables
ten = 5 + 5
print('ten: ', ten)



#*** 8 => Creating counting variables
count = 0
print(count)
count += 1 # OR, count = count + 1
print(count)
count += 1
print(count)


# other shorthand versions for other numerical operators
count -= 2 # count = count - 2
count *= 3 # count = count * 3
count /= 3 # count = count / 3
