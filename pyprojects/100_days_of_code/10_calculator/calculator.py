'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import art
import os


def main():

    try:
        while True:
            
            print(art.logo) 

            is_continue_calculating = True

            # ensure input is numeric
            try:
                first_number = float(input("What's the first number?: "))

            except ValueError as ex:
                # log print("Error casting first number intut to float")
                print("Invalid first number entered." + "\n" + str(ex))
                continue
            

            while is_continue_calculating:
                    
                operation = get_operation()

                if operation == None:
                    print("No math operation selected.")
                    continue

                # ensure input is numeric
                try:                    
                    second_number = float(input("What's the next number?: "))

                except ValueError as ex:
                    print('Invalid second number entered.' + '\n' + str(ex) + '\n')
                    continue
                
                # convert float values back to string for the eval function
                first_number = str(first_number)
                second_number = str(second_number)

                try:
                    evaluation = eval(first_number + ' ' + operation + ' ' + second_number)

                except ZeroDivisionError as ex:
                    print(f"Cannot divide {first_number} by zero.")
                    continue # prevent crashing program and go back to loop to ask for operation               

                result =  first_number + ' ' + operation + ' ' + second_number + ' = ' + str(evaluation)
                print(result)

                keep_calculating = input(f"Type 'y' to continue calculating with {evaluation}, or type 'n' to start a new calculation: ")

                if keep_calculating != 'y':
                    os.system('cls||clear')
                    is_continue_calculating = False     

                else:
                    # reset first number as current evaluation to be used to continue
                    # calculating with next second number inputted.
                    first_number = evaluation

    except Exception as ex:
        print("Error occured." + '\n' + str(ex))


def get_operation():
    ''' 
        function used to list the available operations for the calculator.
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