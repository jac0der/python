'''
    Program to organize my download folder by filtering out
    images, documents and videos when downloaded from the internet.
    
    @datetime:: May 04, 2024 10:27 pm (UTC-5)
    @author:: jac0der
'''


# import modules
import os
import shutil


# declare constants
SOURCE_DIR = '/home/jacoder/Downloads/'


DEST_DIRS = {
    'dest_doc': '/home/jacoder/Documents/download_sorts/',
    'dest_mus': '/home/jacoder/Music/download_sorts/',
    'dest_img': '/home/jacoder/Pictures/download_sorts/',
    'dest_vid': '/home/jacoder/Videos/download_sorts/',
    'dest_unsorted': '/home/jacoder/Documents/download_sorts/noextentions/'
}


DOC_EXTENSIONS = ('.pdf', '.iso', '.txt')
MUS_EXTENSIONS = ('.mp3', '.wav')
IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg')
VID_EXTENSIONS = ('.mov', '.mp4')


def main():
    create_destination_directories()
    extract_file_extensions(get_files())


def create_destination_directories():
    '''
        Function to check if all the destination directories
        already exists, if not, create destination directory.
    '''
    # create the destination path if it doesnt exists.
    for destination_path in DEST_DIRS.values():
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)


def get_files():
    '''
        Function to get all the files within source directory
        to be processed for moving.

        @input:: none
        @output:: iterator of all files within source directory.
    '''
    files = os.scandir(SOURCE_DIR)
    return files


def extract_file_extensions(files):
    '''
        Function to loop over all the files in source directory,
        and move out files to their respective destination directories
        based on the file extensions.
    '''
    for file in files:
        file_name = file.name # get each file name
        source_file_path = file.path

        # check file_name for a period(.)
        # If there is no period, catch raised ValueError and 
        # set last_index to -1
        try:
            last_index = file_name.rindex('.')
        except ValueError:
            last_index = -1

        # get file extension
        if last_index >= 0:
            # substring file name from last period index to end of file_name
            file_extension = file_name[last_index:].lower().strip() 
        else:
            file_extension = None

        if file_extension in DOC_EXTENSIONS:
            # copy file to documents destination folder
            move_file(source_file_path, DEST_DOC + file_name)

        elif file_extension in MUS_EXTENSIONS:
            move_file(source_file_path, DEST_MUS + file_name)

        elif file_extension in IMG_EXTENSIONS:
            move_file(source_file_path, DEST_IMG + file_name)

        elif file_extension in VID_EXTENSIONS:
            move_file(source_file_path, DEST_VID + file_name)

        else:
            # copy file without extension to unsorted folder
            move_file(source_file_path, DEST_UNSORTED + file_name)  


def move_file(source_file_path, destination_file_path):
    shutil.move(source_file_path, destination_file_path)


if __name__ == "__main__":
    main()