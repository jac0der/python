'''
    Exploring python's printing to the console.

    @datetime:: October 02, 2024 11:03 pm (UTC-5)
    @author:: jac0der
'''
# syntax => print(object= separator= end= file= flush=)


#*** 1 => simple printing
print("Welcome to jacoder coding!")
print("Welcome to Jamrock!")


#*** 2 => concatenating strings
print("God is", "a Good", "God") # dont have to space when using commas, items spaced automatically
print("Well done " + "thou good and" + " faithful servant")

# using f-string
fruit = "Peach"
sport = "football"
hobby = "reading"
print(f"{fruit} is my favorite fruit.")

# using string.format()
# I can specify the order in which they are printed by using numbers (tuple index)
thningsme = "I enjoyed playing {} growing up as a child, but I also like {} after school.".format(sport, hobby)
print(thningsme)


#*** 3 => print() with the end= parameter
# newline at end of print
print("This is the first line.", end='\n')
print("New line print starts here.\n")

# tab at end of print
print("This is a tab test.", end='\t\t')
print("After tab at end.")


#*** 4 => print() with the sep= parameter
print("November 5", "is the biggest election", "for the USA.", "asdfg",sep=' | ')


#*** 4 => print() with the file= parameter to output to a file
sample = open('samplefile.txt', 'w')
 
print('Print to a file', file= sample)
sample.close()
