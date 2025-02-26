''' 
Explore global scope in Python.

@datetime:: February 25, 2025 10:35 pm (UTC-5)
@author:: jac0der
'''

'''
Global scope is defining variables outside fuctions. 
So global variables can be accessed within functions as well
as outside of functions.
'''

# global scope variable
score = 77

def get_score():
    print(f"Initial score is {score}")

get_score()
print(score)