# set constants for ascii letter range to use to find letters in text
ASCII_LOWER_BOUND = "A"
ASCII_UPPER_BOUND = "Z"

# get text input from user.
text = input("Text: ")


"""
    Function to count the letters in the text entered by user.
    Text is first converted to ALL CAPPS, to be able to only check
    for letters in ASCII which falls in the range of 65 (A) - 90 (Z).
    Once the ascci value of the character falls within the aforementioned
    range, then a letter is found.
    @input:: text:: Text to examine for Grade Level.
    @output:: Total amount of letters in the input text.
"""


def count_letters(text):
    letter_count = 0

    # set text to ALL CAPS
    text = text.upper()

    # loop the text and check if the ascii values of each character falls within the ascii
    # value range for ALL CAPS letters, using the ord method.
    for c in text:
        if ord(c) >= ord(ASCII_LOWER_BOUND) and ord(c) <= ord(ASCII_UPPER_BOUND):
            letter_count += 1

    return letter_count


"""
    Function to count the words in the text entered by user.
    First the text is striped of any spaces at the start or end
    of the text. Then the text is split by and space to get a List
    of all the sequences of words within the text.
    The words List length is then obtained as the word count of text.
    @input:: Text:: Text to examine for Grade Level.
    @output:: Total amount of words in the input text.
"""


def count_words(text):
    # convert text to a List of words, then return length of words List
    words = text.strip().split(" ")
    return len(words)


"""
    Function to count the sentences in the text entered by user.
    Any occurrence of a period, exclamation point, or question mark
    indicates the end of a sentence.
    Thus, simply count each of the ./?/! which would indicate the
    amount of sentences.
    @input:: text: Text to examine for Grade Level.
    @output:: Total amount of sentences in the input text.
"""


def count_sentences(text):
    # count up end of sentence punctuations
    q = text.count("?")
    e = text.count("!")
    p = text.count(".")

    return q + e + p


"""
    Function to calculate the Coleman Liau Index for entered text.
    @input:: text: Text to examine for Grade Level.
    @output:: Coleman Liau Index Grade Level Index for text.
"""


def caluculateColemanLiauIndex(text):
    word_count = count_words(text)

    L = (count_letters(text) / word_count) * 100
    S = (count_sentences(text) / word_count) * 100

    # round to the nearest integer
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        return "Before Grade 1"
    elif index >= 16:
        return "Grade 16+"
    else:
        return "Grade " + str(index)


print(caluculateColemanLiauIndex(text))
