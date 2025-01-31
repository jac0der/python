'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import art


def main():

    try:
        while True:
            
            print(art.logo) 

            is_continue_calculating = True

            first_number = float(input("What's the first number?: "))

            while is_continue_calculating:
                    
                operation = get_operation()

                if operation == None:
                    print("No math operation selected.")
                    return 0

                second_number = float(input("What's the next number?:"))

                first_number = str(first_number)
                second_number = str(second_number)

                try:
                    evaluation = eval(first_number + ' ' + operation + ' ' + second_number)

                except ZeroDivisionError as ex:
                    print(f"Cannot divide {first_number} by zero.")
                    continue # prevent crashing program and go back to loop to ask for operation               

                result =  first_number + ' ' + operation + ' ' + second_number + ' = ' + str(evaluation)

                keep_calculating = input(f"Type 'y' to continue calculating with {evaluation}, or type 'n' to start a new calculation: ")

                if keep_calculating != 'y':
                    is_continue_calculating = False
                else:
                    # reset first number as current evaluation to be used to continue
                    # calculating with nex second number.
                    first_number = evaluation

    except Exception as ex:
        print("Error occuredfd." + '\n' + str(ex))


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