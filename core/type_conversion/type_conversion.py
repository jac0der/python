'''
    Exploring type conversion in python.

    @datetime:: September 06, 2025 8:07 am (UTC-5)
    @author:: jac0der
'''

# implicit type conversion

#*** 1 => automatic conversion of int to float in addition arithmetic
bill_amount = 145.47
tip = 5

total = bill_amount + tip       # tip (int) is automatically converted to float
print(total)        # 150.47
print(type(total))  # <class 'float'>


#*** 2 => automatic conversion of int to float in multiplication arithmetic
persons = 25
cost_per_person = 3.67

product = persons * cost_per_person     # persons (int) is automatically converted to float
print(product)          # 91.75
print(type(product))    # <class 'float'>


#*** 3 => implicit type conversion for integer division - integer division gives float
fruits = 14
children = 7

portions = fruits / children # result portions is automatically converted into float by python
print(portions)         # 2.0
print(type(portions))   # <class 'float'>