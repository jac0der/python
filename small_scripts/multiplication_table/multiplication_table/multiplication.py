'''
    Generate the multiplication table of a number.

    @datetime:: February 10, 2025 9:50 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
import multiplication_error as me
import multiplication_constants as mc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('multiplication', './multiplication.log')


def get_number():
    '''
    Get a number to generate multiplication table.
    Returns:
            int: User-entered number for the multiplication table.
    '''
    logger.info('Getting number from user.')
    while True:
        try:
            user_input = input("\nEnter number (q to quit): ").strip().lower()

            if user_input == 'q':
                exit_program(pcc.EXIT_MESSAGE)

            number = int(user_input)

            if number < 0:
                raise me.MultiplicationTableError(pcc.INVALID_NUMBER)

            print(mc.ENTERED_NUMBER.format(number))
            logger.info(mc.ENTERED_NUMBER.format(number))

            return number

        except ValueError as ex:
            print(mc.GET_NUMBER_WARNING)
            logger.warning(f'{mc.GET_NUMBER_WARNING} \n {ex}')

        except pce.MultiplicationTableError as ex:
            print(mc.INVALID_NUMBER)
            logger.warning(f'{mc.INVALID_NUMBER} \n {ex}')


def exit_program(message, code=0):
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main():
    """ Main function to start the multiplication table program. """
    try:
        logger.info('Starting the multiplication table program.')
        while True:            
            number = get_number()

    except (KeyboardInterrupt, EOFError):
        print(f"\n{mc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Prime Checking function.")


if __name__ == "__main__":
    main()