'''
    Program to organize my download folder by filtering out
    images, documents and videos when downloaded from the internet.
    
    @datetime:: May 04, 2024 10:27 pm (UTC-5)
    @author:: jac0der
'''


# import modules
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# declare constants
SOURCE_DIR = '/home/jacoder/Downloads/'


DEST_DIRS = {
    'dest_doc': '/home/jacoder/Documents/download_sorts/',
    'dest_mus': '/home/jacoder/Music/download_sorts/',
    'dest_img': '/home/jacoder/Pictures/download_sorts/',
    'dest_vid': '/home/jacoder/Videos/download_sorts/',
    'dest_unsorted': '/home/jacoder/Documents/download_sorts/noextentions/'
}


DOC_EXTENSIONS = ('.pdf', '.iso', '.txt', '.zip')
MUS_EXTENSIONS = ('.mp3', '.wav')
IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp')
VID_EXTENSIONS = ('.mov', '.mp4', '.webm')


def main():
    create_destination_directories()

    #print('debouncing/delaying for 7 seconds...', end='\n')
    #time.sleep(7)

    files = get_files()

    if files is not None:
        extract_file_extensions(files)

    else:
        print(f'No files currently exists in source directory {SOURCE_DIR}')
    
    print()
    print("\nWatcher Running in {}\n".format(SOURCE_DIR))
    print()


def create_destination_directories():
    '''
        Function to check if all the destination directories
        already exists, if not, create destination directory.

        @input:: none
        @output:: none
    '''
    # create the destination path if it doesnt exists.
    for destination_path in DEST_DIRS.values():
        if not os.path.exists(destination_path):
            try:
                os.mkdir(destination_path)

            except FileNotFoundError:
                print(f'Destination directory {destination_path} doesn''t exists.')


def get_files():
    '''
        Function to get all the files within source directory
        to be processed for moving.

        @input:: none
        @output:: iterator of all files within source directory.
    '''
    files = None

    try:
        files = os.scandir(SOURCE_DIR)
        
    except FileNotFoundError:
        print(f'Source directory {SOURCE_DIR} doesnt exists.')    

    return files


def extract_file_extensions(files):
    '''
        Function to loop over all the files in source directory,
        and move out files to their respective destination directories
        based on the file extensions.

        @input:: iterator -> files collection with all files found within the
                             source directory.
        @output:: none
    '''
    is_next_file = False

    try:
        for file in files:
            # get the file size  to loop and check if file has been
            # completly created/downloaded within the source directory.
         #   file_size = file.stat().st_size
            try:
                initial_file_size = file.stat().st_size
            except Exception as e:
                print(e)
                print('file named: {}'.format(file.name) + 'missing...')
                continue
            
            file_name = file.name # get each file name
            source_file_path = file.path # get each absolute file path

            # check if the file size has stopped changing, which
            # indicates that the file has been fully written or downloaded.
            while True:
                print('in while...')
                # delay to check for file size change, which would mean
                # file is not fully written as yet.
                time.sleep(1)
                try:
                    new_file_size_check = os.path.getsize(file.path)

                    print('file size ' + str(initial_file_size))
                    print('new file size ' + str(new_file_size_check))

                    if new_file_size_check == initial_file_size:
                        # file completly written to directory so break from
                        # loop and move file
                        break
                    else:
                        initial_file_size = new_file_size_check

                        # if file size just never stabilizes, check if timeout
                        # point is reached to exit loop, preventing an infinite loop.

                except Exception as e:
                    print(e)
                    print('Error checking if file has been fully written.')
                    is_next_file = True
                    break # break to prevent infinite loop

            if is_next_file:
                continue   # move to next file

            # check file_name for a period(.)
            # If there is no period, catch raised ValueError and 
            # set last_index to -1
            try:
                # find last period (.) in filename
                last_index = file_name.rindex('.')
            except ValueError:
                last_index = -1
            except Exception as e:
                print(e) # if I try to get index of a file which no longer exists

            # get file extension
            if last_index >= 0:
                # substring file name from last period index to end of file_name
                file_extension = file_name[last_index:].lower().strip() 
            else:
                file_extension = None

            if file_extension in DOC_EXTENSIONS:
                # copy file to documents destination folder
                move_file(source_file_path, DEST_DIRS['dest_doc'], file_name)

            elif file_extension in MUS_EXTENSIONS:
                move_file(source_file_path, DEST_DIRS['dest_mus'], file_name)

            elif file_extension in IMG_EXTENSIONS:
                move_file(source_file_path, DEST_DIRS['dest_img'], file_name)

            elif file_extension in VID_EXTENSIONS:
                move_file(source_file_path, DEST_DIRS['dest_vid'], file_name)

            else:
                # copy file without extension to unsorted folder
                move_file(source_file_path, DEST_DIRS['dest_unsorted'], file_name, False)

    except Exception:
        print('Error in extract_file_extensions(files) method.')


def move_file(source_file_path, destination_file_path, filename, is_extension = True):
    '''
        Function to move a file from a source directory 
        to a destination directory.

        @inputs:: 
                 source_file_path:str -> absolute source file path of file to move.
                 destination_file_path:str -> destination file path to move file to.
                 filename:str -> name of the file to be copied to destination.
                 is_extension:bool -> optional parameter flag used to indicate whether
                                      filename passed in has a valid extension checked for.
        @output:: none
    '''
    # check if file already exists, if so add counter increment to the new file being 
    # copied to make it a unique filename.
    counter = 2

    try:
        while True:
            # check if file exists before trying to copy file to destination
            if os.path.exists(destination_file_path + filename):

                if is_extension:
                    parts = filename.split('.')
                    filename = parts[0] + str(counter) + '.' + parts[1]

                else:
                    filename = filename + str(counter)

                counter += 1
            else:
                break

        shutil.move(source_file_path, destination_file_path + filename)

    except Exception as e:
        print(e)
        print(f'Error moving file {filename} to destination {destination_file_path}.')


class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")
    

class MonitorDocumentCreation(FileSystemEventHandler):

    def on_created(self, event):

        # only process files, not directories
        if not event.is_directory:
            main()


if __name__ == "__main__":
    w = Watcher(SOURCE_DIR, MonitorDocumentCreation())
    w.run()