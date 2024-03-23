'''
    conditionals are used to make decision in programming.
    Execute an action but only if a specific condition is met
    
    @datetime:: March 23, 2024 12:55 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => General structure of if statement
# if condition is True, perform action, otherwise do nothing.
"""

if condition:
    Action

"""

#*** 2 => example: If someone clicks a like button, add a like to our counter (increment like variable).
# declare boolean variable
click = False   # nothing has been clicked as yet.
Like = 0

click = True

if click == True:       # equality check - is click and True the same value
    Like = Like + 1     # global variable
    click = False       # reset click to False

print(Like)


#*** 3 => check if a variable is >, <, <=, >= a value
Temperature = 20  # degrees
Thermo = 15

print(Thermo)

if Temperature <= 15:
    Thermo = Thermo + 5

print(Thermo)


#*** 4 => if temperatue is too hot then turn it down the thermostat even some more.
if Temperature >= 20:
    Thermo = Thermo - 3

print(Thermo)


#*** 5 => examples with words and logical operators
Time = "Day"
Sleepy = False
Pajamas = "UNKNOWN"

print(Pajamas)

if Time == "Night" and Sleepy == True:
    Pajamas = "On"

print(Pajamas)

if Time == "Night" or Sleepy == True:
    Pajamas = "On"

print(Pajamas)


#*** 6 => check for multiple conditions - elif
if Time == "Night":
    Pajamas = "On"

elif Time == "Morning":
    Pajamas = "On"

else:
    Pajamas = "Off"

print(Pajamas)