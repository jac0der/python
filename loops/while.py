'''
    A while loop is used to perform an action 
    as long as a specified condition is true.

    @datetime:: September 15, 2024 11:35 pm (UTC-5)
    @author:: jac0der
'''


x = 1

while x < 10:
    print(f'x is: {x}')
    x += 1 # increment value of x to prevent infinite loop


try:
    number = int(input("Enter a number: "))

    while(number < 4 or number > 8):
        number = int(input("Enter a number: "))

    print(f'success number is: {number}')

except Exception:
    print('Invalid input, please enter a number.')
