'''
    Program to load lines from a file containing words to be 
    added to a dictionary, represented by a set(), as set()s
    allows only unique values.

    The dictionary may then be searched for specified words.
    
    @datetime:: November 01, 2023 11:32 pm (UTC-5)
    @author:: jac0der
'''


# initializing the dictionary
words = set()


"""
    main function for pprogram...
"""
def main():
    # loading words from file into memory
    load('large')
    print(words)
    print()

    # get the size of the dictionary
    print('Size of dictionary:', size())

    # check if the word beer is in the dictionary
    print('Word beer in dictionary?', check('beer'))


"""
    function to check for a specified word to see if it
    exists within the dictionary.
"""
def check(word):
    if word.lower() in words:
        return True
    else:
        return False


"""
    function to load the words into the dictionary
"""
def load(dictionary):
    # load dictionary into memory, returning true if successful else false
    file = open(dictionary, 'r')
    for line in file:
        word = line.rstrip()
        words.add(word)
    
    file.close()

    return True


"""
    function to get the size of the dictionary.
"""
def size():
    # returns number of words in dictionary if loaded else 0 if nto yet loaded
    return len(words)


"""
    free up any memory utilize - done automatically by python
"""
def unload():
    # unloads tionary from memory, returning true if successful, else false
    return True    


main()





