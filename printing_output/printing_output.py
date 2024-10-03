'''
    Exploring python's printing to the console.

    @datetime:: October 02, 2024 11:03 pm (UTC-5)
    @author:: jac0der
'''
#*** 1 => simple printing
print("Welcome to jacoder coding!")
print("Welcome to Jamrock!")


#*** 2 => concatenating strings
print("God is", "a Good", "God") # dont have to space when using commas
print("Well done " + "thou good and" + " faithful servant")

# using f-string
fruit = "Peach"
sport = "football"
hobby = "reading"
print(f"{fruit} is my favorite fruit.")

# using string.format()
thningsme = "I enjoyed playing {0} growing up as a child, but I also like {1} after school.".format(sport, hobby)
print(thningsme)

print("hello", file='testtt')
