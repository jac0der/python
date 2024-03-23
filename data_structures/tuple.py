'''
    Tuple is an ordered sequence of items same as a list. 
    The only difference is that tuples are immutable. 
    Tuples once created cannot be modified.
    
    @datetime:: March 22, 2024 10:34 pm (UTC-5)
    @author:: jac0der
'''

#*** 1 => creating a tuple
numbers = (1, 2, -5, 'hello')
print(numbers)

# create tuple with tuple constructor
tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)

# create an empty tuple
empty_tuple = ()
print(empty_tuple)



#*** 2 => access tuple item
dimensions = (500, 800)
print(dimensions[1])  # 800



#*** 3 => tuple length
print(len(dimensions))



#*** 4 => Iterate through a tuple
car_brands = ('toyota', 'subaru', 'mitsubishi', 'lexus', 'skyline')
print(car_brands)

for brand in car_brands:
    print(brand)



#*** 5 => check if item exists in tuple
print('subaru' in car_brands)
print('evo' in car_brands)



#** 6 => delete tuple
# I cannot delete individual items of a tuple, but I can delete the tuple 
# itself using the del statement.
animals = ('dog', 'cat', 'rat')
print(animals)
del animals



#*** 7 => create a tuple with one item - must put the training comma
var = ('hello', )



















