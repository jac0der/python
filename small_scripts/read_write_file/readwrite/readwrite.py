'''
create a program to read a file, modiify its content,
and write back to a new file.

@datetime:: September 18, 2025 10:49 pm (UTC-5)
@author:: jac0der
'''


from logging_custom import jaclog
logger = jaclog.configure('read_write', './read_write.log')


def main()->None:
    """ Main function to start the read write file program. """
    try:
        logger.info("Start the file read write program.")

    except Exception as ex:
        logger.exception("Error occurred in main Read Write Fidle function.")


if __name__ == "__main__":
    main()