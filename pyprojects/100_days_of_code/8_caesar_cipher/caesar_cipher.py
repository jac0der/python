"""
    Create a program to use the caesar cipher method
    of encrypting data by a particular shift amount.
    Also implement a dycrypt method to reverse an encrypted
    caesar cipher text.
    
    @datetime:: December 08, 2024 8:47 pm (UTC-5)
    @author:: jac0der
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(encrypt(text, shift))


# TODO-1: Create a function called 'encrypt()' that takes original_text and shift_amount as 2 inputs.
def encrypt(original_text, shift_amount):
    pass


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
# by the shift amount and print the encrypted text.
def encrypt(original_text, shift_amount):

    cipher = ''
    
    for letter in original_text:
        # get the index position for letter
        index = alphabet.index(letter)
        shift_index = index + shift_amount

        if shift_index > 25:
            shift_index = shift_index % 25

        shift_letter = alphabet[shift_index]
        cipher += shift_letter

    return cipher


if "__name__" == "__main__":
    main()

# TODO-4: What happens if I try to shift z forwards by 9? Can I fix the code?

  
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. I should be able to test the code and
# encrypt a message