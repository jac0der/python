"""
    Create a program to use the caesar cipher method
    of encrypting data by a particular shift amount.
    Also implement a dycrypt method to reverse an encrypted
    caesar cipher text.
    
    @datetime:: December 08, 2024 8:47 pm (UTC-5)
    @author:: jac0der
"""


# constant alphabet list of letters
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    '''
        Entry point to the caesar cipher program.
        Accepts user inputs and decide whether to encode or decode text.
    '''
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(f'Here is the encoded result: {encrypt(text, shift)}')


# by the shift amount and print the encrypted text.
def encrypt(original_text, shift_amount):
    '''
        function to create a caesar cipher encrypted text based on a specified
        amount of shifts.

        @inputs:: original_text-> str: the text entered by user to be encrypted.
                  shift_amounbt-> int: the amount of shifts to be appied to original_text.
        
        @output:: cipher-> str: the encrypted caesar cipher by specified shift amount.
    '''
    cipher = ''
    
    for letter in original_text:
        # get the index position for letter
        index = ALPHABET.index(letter)
        shift_index = index + shift_amount

        # check if the shift amount plus current index of letter out range of 25 (z)
        # if so find the modulus of that number with length of ALPHABET list (26)
        if shift_index > len(ALPHABET):
            shift_index %= len(ALPHABET) # ensure stay withjin range of 0-25

        shift_letter = ALPHABET[shift_index]
        cipher += shift_letter

    return cipher


if __name__ == "__main__":
    main()