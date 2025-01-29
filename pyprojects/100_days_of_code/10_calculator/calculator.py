'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import art


def main():
    print(art.logo)

    first_number = int(input("What's the first number?: "))
    operation = get_operation()

    if operation == None:
        print("No math operation selected.")
        return 0


def get_operation():
    ''' 
        function used to list the available operations 
        for the calculator.
        @input:: none
        @output:: selected math operation, otherwise, None - indicating
                  math operation was not successfully selected.
    '''
    operation = None

    try:
        is_choose_operation = True
        operations = ['+', '-', '*', '/']

        for op in operations:
            print(op)
        
        while is_choose_operation:
            operation = input("Pick an operation: ").strip()

            if operation in operations:
                is_choose_operation = False
                
    except Exception as ex:
        print("Error choosing math operation. " + '\n' + str(ex))
        return None

    return operation

    


if __name__ == "__main__":
    main()