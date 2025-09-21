'''
    Generate the multiplication table of a number.

    @datetime:: February 10, 2025 9:50 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
from logging_custom import jaclog
import multiplication_error as me
import multiplication_constants as mc

logger = jaclog.configure('multiplication', './multiplication.log')


def get_number(prompt, default=None):
    '''
    Get a number to generate multiplication table.
    Returns:
            int: User-entered number for the multiplication table.
    '''
    logger.info('Getting number or range from user.')
    while True:
        try:
            user_input = input(prompt).strip().lower()

            if user_input == 'q':
                exit_program(mc.EXIT_MESSAGE)

            # This lets users hit Enter to use the default range.
            if default is not None and user_input == "":
                return default

            number = int(user_input)

            if number < 0:
                raise me.MultiplicationTableError(pcc.INVALID_NUMBER)

            return number

        except ValueError as ex:
            print(mc.GET_NUMBER_WARNING)
            logger.warning(f'{mc.GET_NUMBER_WARNING} \n {ex}')

        except me.MultiplicationTableError as ex:
            print(mc.INVALID_NUMBER)
            logger.warning(f'MultiplicationTableError: {ex}')


def generate_times_table(number:int, range_number:int=mc.DEFAULT_RANGE):
    '''
    Generate the multiplication times table for a number up to the
    specified range.

    Args:
        number (int): The number times table to generate.
        range (int): Limit up to which number to generate the
                     the times table.
    '''
    if not isinstance(number, int) or not isinstance(range_number, int):
        raise ValueError('Invalid Type: Expected an integer.')

    if number < 0 or range_number < 0:
        raise me.MultiplicationTableError(mc.INVALID_NUMBER)

    header = f'\nGenerating Multiplication table for {number} up to {range_number}.'
    print(header)
    logger.info(header)

    # list comprehension
    table_lines = [f"\t{number} * {n} = {number * n}" for n in range(1, range_number + 1)]
    table_output = "\n".join(table_lines)

    print(table_output)
    logger.info(table_output)


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
            number = get_number("\nEnter number for multiplication table (q to quit): ")
            print(mc.ENTERED_NUMBER.format('Number', number))
            logger.info(mc.ENTERED_NUMBER.format('Number', number))

            range_number = get_number("\nEnter range (default is 12) (q to quit): ", mc.DEFAULT_RANGE)
            print(mc.ENTERED_NUMBER.format('Range', range_number))
            logger.info(mc.ENTERED_NUMBER.format('Range', range_number))

            generate_times_table(number, range_number)

    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except me.MultiplicationTableError as ex:
        logger.error(f"MultiplicationTableError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{mc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Multiplication Generation function.")


if __name__ == "__main__":
    main()