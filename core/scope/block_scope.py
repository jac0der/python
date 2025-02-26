''' 
Block scopes in Python

@datetime:: February 25, 2025 10:35 pm (UTC-5)
@author:: jac0der
'''

'''
Variables declared within code blocks if, while, for etc...
are only accessible within the defining code blocks.
'''

age = 25

if age > 70:
    senior = "John"
    print("good age")

print(age)
#print(senior) # NameError: name 'senior' is not defined

while True:
    price = 2
    break

print(price)