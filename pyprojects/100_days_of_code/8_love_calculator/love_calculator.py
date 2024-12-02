
TRUE_SEARCH = "true"
LOVE_SEARCH = "love"

def main():
    love_score = calculate_love_score("Angela Yu", "Jack Bauer")
    print(love_score)


def calculate_love_score(name1, name2):
    '''
    '''
    # set up counter variables tp 0 initially
    true_counter = 0
    love_counter = 0

    # ensure input names are lowercase and without white spaces
    name1 = name1.lower().strip()
    name2 = name2.lower().strip()

    true_love_name = name1 + name2

    for tletter in TRUE_SEARCH:
        
        for letter in true_love_name:
            if tletter == letter:
                true_counter += 1

    for lletter in LOVE_SEARCH:
        
        for letter in true_love_name:
            if lletter == letter:
                love_counter += 1

    return str(true_counter) + str(love_counter)


if __name__ == "__main__":
    main()
    
    
