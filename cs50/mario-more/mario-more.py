def main():
    height = get_height()

    # ignore index 0 from range function and go up to entered height plus 1
    for count in range(1, height + 1):
        spaces = " " * (height - count)
        hash_prints = "#" * count

        # print pyramid - left spaces, left hashes #, 2 spaces, right hashes #
        print(spaces + hash_prints + "  " + hash_prints)
    """
        print(spaces, end='')
        print("#" * count, end='')
        print("  ", end='')
        print("#" * count)
    """


def get_height():
    while True:
        try:
            # trying to cast input by user, if fail to cast input
            # to an integer, then just loop until a valid input is entered.
            height = int(input("Height: "))

        except ValueError:
            continue


        if height > 0 and height < 9:
            return height


main()