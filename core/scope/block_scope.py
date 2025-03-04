''' 
Block scopes in Python

@datetime:: February 25, 2025 10:35 pm (UTC-5)
@author:: jac0der
'''

'''
The while/if block does not create a new scope in Python. 
Variables declared inside loops (or if statements) are part of the same scope 
as the surrounding code unless they are inside a function or class.
'''

age = 71

if age > 70:
    senior = "John"     # global scope
    print("good age")

print(age)
print(senior)


while True:
    price = '2'         # global scope
    break

print(price)