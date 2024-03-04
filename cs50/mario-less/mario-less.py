"""
    main function to start program execution.

    @input:: none.
    @output:: none.
"""
def main():
    height = get_height();
    print_pyramid(height)


"""
    function used to get a positive integer for 
    height of pyramid.
    
    @input::none
    @output::int -> height of pyramid to be printed.
"""
def get_height():

    # loop until a valid input is entered
    while True:
        
        try:
            # get user pyramid height cast to integer
            height = int(input('Height: '))

            if height > 0 and height < 9:
                return height
            else:
                print('enter a positive number')

        except ValueError:
            print('invalid')


"""
    function to print the pyramid based on height
    passed in.

    @input::int -> height of pyramid to print.
    @output: printed pyramid.
"""
def print_pyramid(height):

    hash_count = 1
    space_count = height - 1

    for i in range(height):

        # print spaces on same line
        print(' ' * space_count, end="")
        print('#' * hash_count)

        space_count -= 1
        hash_count += 1 


# start program execution.
if __name__ == "__main__":
    main()