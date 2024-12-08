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

# constant alphabet list of letters
ALPHABET = a.ALPHABET

def main():
    '''
        Entry point to the caesar cipher program.
        Accepts user inputs and decide whether to encode or decode text.
    '''
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":

        cipher_result = encrypt(text, shift)

        if cipher_result != '':
            print(f'Here is the encoded result: {cipher_result}')
        else:
            print('Error occured during cipher generation.')


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


if __name__ == "__main__":
    main()