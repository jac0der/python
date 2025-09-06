'''
    Exploring operators in python.

    @datetime:: September 06, 2025 9:54 am (UTC-5)
    @author:: jac0der
'''

#*** 1 => arithmetic operators
x,y = 8,2

print(f'sum of {x} and {y}: {x + y}')               # 10
print(f'difference of {x} and {y}: {x - y}')        # 6    
print(f'product of {x} and {y}: {x * y}')           # 16
print(f'division of {x} and {y}: {x / y}')          # 4.0
print(f'floor division of {x} and {y}: {x // y}')   # 4 - force integer division
print(f'modulo of {x} and {y}: {x % y}')            # 0    
print(f'power of {x} and {y}: {x ** y}')            # 64


#*** 2 => assignment operators
number = 7
print(number)

number += 1
print(number)

number -= 1
print(number)

number *= 2
print(number)

number /= 2
print(number)

number **= 2
print(number)

number %= 1
print(number)



#*** 3 => comparison operators
patient_count = 20
doctor_count = 18

print(patient_count == doctor_count)    # False     
print(patient_count != doctor_count)    # True
print(patient_count > doctor_count)     # True
print(patient_count < doctor_count)     # False
print(patient_count >= doctor_count)    # True
print(patient_count <= doctor_count)    # False


print()
print('logical ops...', end='\n')
#*** 4 => logical operators
print((5 > 2) and (6 >= 6)) # True   
print((5 < 2) and (6 >= 6)) # False 
print()

print((5 == 5) or (2 > 7))  # True
print((5 != 5) or (2 > 7))  # False

print()
print(not True)  # False
print(not False) # True


print()
#*** 5 => identity operator
a = 10
b = 10
x = [1,2,3]
y = [1,2,3]

print(a is b)       # True
print(b is not a)    # False
print(x is y)       # False



print()
#*** 6 => membership operator
code_languages = ['python', 'c++', 'c#', 'cobalt', 'go', 'rust', 'c']

print('rust' in code_languages)         # True
print('vb' not in code_languages)       # True
print('cobalt' not in code_languages)   # False
print('sql' in code_languages)          # False