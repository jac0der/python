'''
    Program to organize my download folder by filtering out
    images, documents and videos when downloaded from the internet.
    
    @datetime:: May 04, 2024 10:27 pm (UTC-5)
    @author:: jac0der
'''

# import modules
import os


# declare constants
SOURCE_DIR = '/home/jacoder/Downloads/'
DEST_DOC = '/home/jacoder/Documents/download_sorts'
DEST_MUS = '/home/jacoder/Music/download_sorts'
DEST_IMG = '/home/jacoder/Pictures/download_sorts'
DEST_VID = '/home/jacoder/Videos/download_sorts'

DOC_EXTENSIONS = ('.pdf', '.iso', '.txt')
MUS_EXTENSIONS = ('.mp3', '.wav')
IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg')
VID_EXTENSIONS = ('.', '.iso', '.txt')

def main():
    move_files(get_files())


def get_files():
    '''
        Function to get all the files within source directory
        to be processed for moving.

        @input:: none
        @output:: iterator of all files within source directory.
    '''
    files = os.scandir(SOURCE_DIR)
    return files


def move_files(files):
    '''
        Function to loop over all the files in source directory,
        and move out files to their respective destination directories
        based on the file extensions.
    '''
    for file in files:
        pass
        # get file extension



if __name__ == "__main__":
    main()