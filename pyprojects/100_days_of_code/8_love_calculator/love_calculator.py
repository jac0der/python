"""
    The Love Calculator program to calculate the love score from 
    two provided names.
    
    @datetime:: December 01, 2024 11:55 pm (UTC-5)
    @author:: jac0der
"""


TRUE_SEARCH = "true"
LOVE_SEARCH = "love"


def main():
    love_score = calculate_love_score("Angela Yu", "Jack Bauer")
    print(love_score)


def calculate_love_score(name1, name2):
    '''
        Function to calculate the love score from two
        provided name.
    '''
    # set up counter variables to 0 initially
    true_counter = 0
    love_counter = 0

    # ensure input names are lowercase and without white spaces
    name1 = name1.lower().strip()
    name2 = name2.lower().strip()

    # concatenate names together as one for easier searching
    true_love_name = name1 + name2

    # search each letter in TRUE with the names
    for tletter in TRUE_SEARCH:
        
        for letter in true_love_name:
            if tletter == letter:
                true_counter += 1

    #  search each letter in LOVE with the names
    for lletter in LOVE_SEARCH:
        
        for letter in true_love_name:
            if lletter == letter:
                love_counter += 1

    love_Score = str(true_counter) + str(love_counter)

    return love_Score


if __name__ == "__main__":
    main()
    
    
