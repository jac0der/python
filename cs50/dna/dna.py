import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # define List to store each of the rows from csv as a List of dictionaries
    database = []

    # define dictionary to store each str and its associated match counts in dna sequence
    match_str_counts = {}

    # Read database file into a variable
    with open(sys.argv[1], "r") as file:
        str_counts = csv.DictReader(file)

        for str_count in str_counts:
            database.append(str_count)

    # Read DNA sequence file into a dna_sequence variable
    with open(sys.argv[2], "r") as sequence:
        dna_sequence = sequence.read()
        sequence.closed

    # get all the STRs to search for in dna sequence
    # get the keys List for the 1st row of csv of the 1st dictionary in List,
    # then return slice of keys not including the first column which is the name of person.
    strs = list(database[0].keys())[1:]

    # Find longest match of each STR in DNA sequence
    for str in strs:
        str_length = longest_match(dna_sequence, str)

        # store match counts for each of the STRs, in a dictionary
        match_str_counts[str] = str_length

    # Check database for matching profiles
    # database is a List of Dictionaries
    is_match = False

    # loop through dictionary person and their str counts obtained from reading in csv file
    for person in database:
        # loop list of strs to be used to compare each person str counts with the matched str counts
        for str in strs:
            if int(person[str]) == int(match_str_counts[str]):
                is_match = True

            else:
                is_match = False
                break

        if is_match:
            print(person["name"])
            break  # exit outter for loop

    if not is_match:
        print("No match")

    return 0


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
