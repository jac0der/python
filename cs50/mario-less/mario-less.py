while True:
    try:
        # try cast input from user to integer
        height = int(input("Height: "))
    
    except ValueError:
        continue

    # check for valid user pyramid height entered
    if height > 0 and height < 9:
        
        # ignore index 0 from range function and go up to entered height plus 1
        for count in range(1, height + 1):
            spaces = " " * (height - count)
            hash_prints = "#" * count

            # print pyramid - left spaces, left hashes #, 2 spaces, right hashes #
            print(spaces + hash_prints)

        # terminate loop after printing pyramid
        break