'''
    Print the first n numbers of the Fibonacci sequence.

    @datetime:: February 9, 2025 8:28 am (UTC-5)
    @author:: jac0der
'''
import fibonacci_constants as fc


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
    """ Main function to start the Fibonacci Program. """
    try:
        pass

    except KeyboardInterrupt as ex:
        exit_program(f"\n{fc.EXIT_MESSAGE}")

    except EOFError as ex:
        exit_program(f"\n{fc.EXIT_MESSAGE}")

    except Exception as ex:
        logger.exception("Error occurred in main Fibonacci function.")


if __name__ == "__main__":
    main()