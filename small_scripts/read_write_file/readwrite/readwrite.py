'''
create a program to read a file, modiify its content,
and write back to a new file.

@datetime:: September 18, 2025 10:49 pm (UTC-5)
@author:: jac0der
'''

import readwrite_constants as rwc
from logging_custom import jaclog
logger = jaclog.configure('read_write', './read_write.log')


def modify_file(input_file:str, output_file:str)->None:
    '''
        Read the contents of a file, modifyies the contents
        of the file, then write modified file contents to a 
        new file.

        Args:
            input_file (str): file to read contents to be modified.
            output_file (str): new file containing the modified contents.
    '''
    # Read all lines from the input file
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Process lines and modify content
    modified_lines:list = [line.replace('tuple', 'Tuple') for line in lines]

    # Write modified content to the output file
    with open(output_file, "w") as file:
        file.writelines(modified_lines)
    
    print(f"File processed successfully. Output written to {output_file}")


def main()->None:
    """ Main function to start the read write file program. """
    try:
        logger.info("Start the file read write program.")
        modify_file(rwc.INPUT_FILE, rwc.OUTPUT_FILE)

    except Exception as ex:
        logger.exception("Error occurred in main Read Write Fidle function.")


if __name__ == "__main__":
    main()