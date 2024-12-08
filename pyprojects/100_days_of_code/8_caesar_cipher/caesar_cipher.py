"""
    Create a program to use the caesar cipher method
    of encrypting data by a particular shift amount.
    Also implement a dycrypt method to reverse an encrypted
    caesar cipher text.
    
    @datetime:: December 08, 2024 8:47 pm (UTC-5)
    @author:: jac0der
"""
# import the alphabet list
import alphabet as a
from art import logo

# constant alphabet list of letters
ALPHABET = a.ALPHABET


def main():
    '''
        Entry point to the caesar cipher program.
        Accepts user inputs and decide whether to encode or decode text.
    '''
    print(logo)
    running = True

    while running:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
        text = input("Type your message:\n").lower()

        try:
            shift = int(input("Type the shift number:\n"))

        except ValueError:
            print("Invalid shift amount entered. Only Numeric values allowed.")
            continue

        if direction not in ('encode', 'decode'):
            print('Invalid operation option entered.')
            continue

        if text == '':
            print('No text entered to encrypt/decrypt.')
            continue

        response = caesar(direction, text, shift)

        if response == '':
            print("Error occured.")
            continue

        print(f'Here\'s the {direction}d result: {response}', end='\n')
        goagain = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n\t").strip().lower()

        if goagain != 'yes':
            print("Bye! Bye!")
            running = False

def caesar(direction, original_text, shift_amount):
    '''
        function to perform a caesar encrypt or decrypt based on the
        direction variable of either encode or decode.

        @inputs:: direction-> string: indicator to either perform encrypt or
                                      decrypt.
                  original_text-> str: the text entered by user to be encrypted/decrypted.
                  shift_amounbt-> int: the amount of shifts to be appied to original_text.
        
        @output:: message-> str: the encrypted caesar cipher by specified shift amount or
                                 the plain_text decrypted cipher or an empty string indicating an error.
    '''
    output_value = ''

    try:
        # set shift to be negative when decrypting
        if direction == "decode":
            shift_amount *= -1

        for letter in original_text:

            # if current letter is not actually a letter but a symbol or number...
            # just add it back to the output value.
            if letter not in ALPHABET:
                output_value += letter
                continue

            # get the current index position for letter
            index = ALPHABET.index(letter) 
            shift_index = index + shift_amount

            # check if the shift amount plus current index of letter out range of 25 (z)
            # if so find the modulus of that number with length of ALPHABET list (26)
            if shift_index >= len(ALPHABET):
                shift_index %= len(ALPHABET) # ensure stay within range of 0-25

            shift_letter = ALPHABET[shift_index]
            output_value += shift_letter

    except Exception:
        # error occured during cipher generation, so log message and return empty string
        return ''

    return output_value

'''
    message = ''

    if direction == "encode":
        cipher_result = encrypt(original_text, shift_amount)

        if cipher_result != '':
            message = f'Here is the encoded result: {cipher_result}'
        else:
            message = 'Error occured during cipher generation.'
            
    elif direction == "decode":
        plain_text = decrypt(original_text, shift_amount) 

        if plain_text != '':
            message = f'Here is the decoded result: {plain_text}'
        else:
            message = 'Error occured during decrypting cipher.'

    else:
        message = 'Invalid option entered.'

    return message
'''
'''
# by the shift amount and print the encrypted text.
def encrypt(original_text, shift_amount):
    \'''
        function to create a caesar cipher encrypted text based on a specified
        amount of shifts.

        @inputs:: original_text-> str: the text entered by user to be encrypted.
                  shift_amounbt-> int: the amount of shifts to be appied to original_text.
        
        @output:: cipher-> str: the encrypted caesar cipher by specified shift amount.
    \'''
    cipher = ''

    try:
        
        for letter in original_text:

            # get the current index position for letter
            index = ALPHABET.index(letter)
            shift_index = index + shift_amount

            # check if the shift amount plus current index of letter out range of 25 (z)
            # if so find the modulus of that number with length of ALPHABET list (26)
            if shift_index >= len(ALPHABET):
                shift_index %= len(ALPHABET) # ensure stay withjin range of 0-25

            shift_letter = ALPHABET[shift_index]
            cipher += shift_letter

    except Exception:
        # error occured during cipher generation, so log message and return empty string
        return ''

    return cipher


def decrypt(original_text, shift_amount):
    \'''
        function to create a caesar cipher decrypt function to decrypt caesar cipher
        encrypted texts based on a specified amount of shifts.

        @inputs:: original_text-> str: the caesar cipher encrypted text entered by user to be decrypted.
                  shift_amounbt-> int: the amount of shifts to be appied to the cipher for decrypting.
        
        @output:: plain_text-> str: the decrypted plain text of the encrypted caesar cipher.
    \'''
    plain_text = ''

    try:
        
        for letter in original_text:

            # get the current index position for letter
            index = ALPHABET.index(letter)
            shift_index = index - shift_amount

            # check if the shift amount plus current index of letter out range of 25 (z)
            # if so find the modulus of that number with length of ALPHABET list (26)
            if abs(shift_index) >= len(ALPHABET):
                shift_index = (abs(shift_index) % len(ALPHABET)) * -1 # ensure stay withjin range of 0-25

            shift_letter = ALPHABET[shift_index]
            plain_text += shift_letter

    except Exception:
        # error occured during decrypting cipher, so log message and return empty string
        return ''

    return plain_text
'''

if __name__ == "__main__":
    main()