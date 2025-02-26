'''
    Set is an unordered collection of unique items. 
    Set is defined by values separated by commas inside braces {}. 
    Elements within a set CANNOT be duplicated.
    
    @datetime:: March 22, 2024 10:53 pm (UTC-5)
    @author:: jac0der
'''

#*** 1 => creating a set
# create empty set
ids = set()
print(ids)

student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

mixed_set = {'hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# create set from a list
l = [1, 2, 3, 4, 5, 6, 7]
s = set(l)
print('set from a list', s)



#** 2 => duplicate item in a set
numbers ={2, 4, 6, 6, 2, 8}
print(numbers) # {8, 2, 4, 6} set only contain unique items



#*** 3 => add items to a set (add() method)
ids = set()
ids.add(24)
print(ids)



#*** 4 => update a set with items from another set
companies = {'lactose', 'ralph lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print(companies)

phamacy = {'benson', 'york', 'blue bell'}
med_schools = {'top school', 'college', 'college'}

phamacy.update(med_schools)
print(phamacy)



#*** 5 => remove item from a set (discard(), pop())
linux = {'nice', 'netstat', 'dd'}
linux.discard('netstat')
print(linux)

linux.pop()
print(linux)



#*** 6 => iterate over a set
tux_commands = {'sudo', 'su', 'diff', 'pacman'}
for command in tux_commands:
    print(command)



#*** 7 => finf set length
print(len(tux_commands))



#*** 8 => set union
A = {1, 2, 3}
B = {0, 2, 4}

print(A | B)        # {0, 1, 2, 3, 4}
print(A.union(B))   # {0, 1, 2, 3, 4}



#*** 9 => set intersection
C = {1, 3, 5}
D = {1, 2, 3}

print(C & D)               # {1, 3}
print(C.intersection(D))   # {1, 3}



#*** 10 => set difference
E = {2, 3, 5}
F = {1, 2, 6}

print(E - F)            # {3, 5}
print(E.difference(F))  # {3, 5}



#*** 11 => symmetric difference
G = {2, 3, 5}
H = {1, 2, 6}

print(G ^ H)                        # {1, 3, 5, 6}
print(G.symmetric_difference(H))    # {1, 3, 5, 6}



#*** 12 => check if two sets are equal
A = {1, 3, 5}
B = {3, 5, 1}

# if sets have the same elements, then sets are equal

if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')



#*** 13 => set comprehension
word = "programming"

unique_letters = {l for l in word}
print(unique_letters)

#I get all the letters but they are not repeated since sets 
# dont repeat elements.















