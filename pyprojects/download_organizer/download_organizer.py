'''
    Program to organize my download folder by filtering out
    images, documents and videos when downloaded from the internet.

    Downloads folder is watched for when create file events happen, and trigger 
    the moving of files once they are fully downloaded or weritten to disk.

    Each file has 10 minutes in which to complete the download/writting of file,
    after which the file is skipped.
    
    @datetime:: May 04, 2024 10:27 pm (UTC-5)
    @author:: jac0der
'''


# import modules
import os
import time
import logging
import shutil as mv
import datetime as dt
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

DOC_EXTENSIONS = ('.pdf', '.iso', '.txt', '.zip', '.deb', '.rpm')
MUS_EXTENSIONS = ('.mp3', '.wav')
IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp')
VID_EXTENSIONS = ('.mov', '.mp4', '.webm')

LOGGING_DIR = './logs'
TIMEOUT_SECONDS = 600           # set time out for file download to 10 minutes
FILE_PROCESS_DELAY = 5          # delay period to wait before re-checking the file size for comparison
                                # with the initial file size.

# Define separate loggers for errors messages and for info messages.
error_logger = None
info_logger = None


def configure_logging():
    '''
        Function to configure the logging module for errors and info messages
        within the script.

        @input:: none
        @output:: none
    '''
    try:
        # I will be re-assigning error_logger and info_logger variables to different 
        # values so I must use the global keyword.
        global error_logger, info_logger

        # Create logger for error messages
        error_logger = logging.getLogger('error_logger')
        error_logger.setLevel(logging.ERROR)

        # Create handler for error messages
        error_handler = logging.FileHandler(f'{LOGGING_DIR}/pyerror_{str(dt.date.today())}.log')
        error_handler.setLevel(logging.ERROR)

        # Create formatter for error messages
        error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        error_handler.setFormatter(error_formatter)

        # Add the error handler to the error logger
        error_logger.addHandler(error_handler)

        # Create logger for info messages
        info_logger = logging.getLogger('info_logger')
        info_logger.setLevel(logging.INFO)

        # Create handler for info messages
        info_handler = logging.FileHandler(f'{LOGGING_DIR}/pyinfo_{str(dt.date.today())}.log')
        info_handler.setLevel(logging.INFO)

        # Create formatter for info messages
        info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        info_handler.setFormatter(info_formatter)

        # Add the info handler to the info logger
        info_logger.addHandler(info_handler)

    except Exception as e:
        print(e)


def create_destination_directories():
    '''
        Function to check if all the destination directories
        already exists, if not, create destination directory.

        @input:: none
        @output:: none
    '''
    info_logger.info('Start create_destination_directories() function')

    try:
        # create the destination directory if it doesnt exists.
        for destination_path in DEST_DIRS.values():

            try:
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)

            except FileNotFoundError as e:                
                error_logger.error(f'Destination directory {destination_path} doesn''t exists.')
                error_logger.error(e)
            except Exception as e:
                error_logger.error(e)

    except Exception as e:
        error_logger.error('Error creating destination directories. Check destination directory dictionary.')        
    
    info_logger.info('End create_destination_directories() function')


def create_logging_directory():
    '''
        Function to create the logging directory for script
        if logs directory doesn't exists.
    '''
    print('Start create_logging_directory()')

    try:
        # create the logging directory if it doesnt exists.
        try:
            if not os.path.exists(LOGGING_DIR):
                    os.mkdir(LOGGING_DIR)

        except FileNotFoundError as e:
            print(f'Logging directory {destination_path} doesn''t exists.')
            print(e)
        except Exception as e:
            print(e)

    except Exception as e:
        print('Error creating destination directories. Check destination directory dictionary.') 

    print('End create_logging_directory()')


def main():
    info_logger.info('Start main() function')

    files = get_files()
    
    # check if any files were found in destination directory.
    if files is not None:
        extract_file_extensions(files)

    else:
        print(f'No files currently exists in source directory {SOURCE_DIR}')
        info_logger.info(f'No files currently exists in source directory {SOURCE_DIR}')
    
    print()
    print("\nWatcher Running in {}\n".format(SOURCE_DIR))
    info_logger.info("Watcher Running in {}\n".format(SOURCE_DIR))
    print()

    info_logger.info('End main() function')


def get_files():
    '''
        Function to get all the current files within source directory
        to be processed for moving.

        @input:: none
        @output:: iterator of all current files within source directory.
    '''
    info_logger.info('Start get_files() function')

    files = None

    try: 
        files = os.scandir(SOURCE_DIR)
        
    except FileNotFoundError as e:        
        error_logger.error(f'Source directory {SOURCE_DIR} doesnt exists.')
        print(e)
    except Exception as e:
        error_logger.error(e)

    info_logger.info('End get_files() function')

    return files


def extract_file_extensions(files):
    '''
        Function to loop over all the current files in source directory,
        and move out files to their respective destination directories
        based on the file extensions.

        @input:: iterator -> files collection with all files found within the
                             source directory.
        @output:: none
    '''
    info_logger.info('Start extract_file_extensions(files) function')

    is_next_file = False

    try:
        info_logger.info('Iterate the current files in source directory.')

        for file in files:
            info_logger.info('Processing file {}\n'.format(file.name))
            # get the initial file size  to loop and check if file has been
            # completly created/downloaded within the source directory.
            try:
                initial_file_size = file.stat().st_size
                info_logger.info('Get initial file size {}'.format(initial_file_size))

            except Exception as e:
                print(e)
                print('file named: {}'.format(file.name) + 'missing...')
                continue
            
            file_name = file.name           # get each file name
            source_file_path = file.path    # get each absolute file path
            
            start_time = time.time()        # get the current time

            # check if the file size has stopped changing, which
            # indicates that the file has been fully written or downloaded.
            while True:
                info_logger.info('Check for file writing/downloading completeness.')
                # delay to check for file size change, which would mean
                # file is not fully written as yet if file size is still changing.
                time.sleep(FILE_PROCESS_DELAY)

                try:
                    new_file_size_check = os.path.getsize(file.path)

                    info_logger.info('get new file size {}'.format(new_file_size_check))
                    print('file size ' + str(initial_file_size))
                    print('new file size ' + str(new_file_size_check))

                    if new_file_size_check == initial_file_size:
                        info_logger.info('Initial and new file size are equal - file completely written.')
                        # file completly written to directory so break from
                        # loop and move file
                        is_next_file = False
                        break
                    else:
                        initial_file_size = new_file_size_check

                        info_logger.info('Check if timeout is reached.')
                        # if file size just never stabilizes, check if timeout
                        # point is reached (10 minutes) to exit loop, preventing an infinite loop.
                        if (time.time() - start_time) >= TIMEOUT_SECONDS:
                            info_logger.info('Time limit for file download reached. Exiting loop...')
                            
                            # go to next file to process
                            is_next_file = True
                            break   # break to prevent infinite loop

                except Exception as e:
                    error_logger.error(e)
                    error_logger.error('Error checking if file has been fully written.')

                    # go to next file to process
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
                error_logger.error(e) # if I try to get index of a file which no longer exists

            # get file extension
            if last_index >= 0:
                # substring file name from last period index to end of file_name
                file_extension = file_name[last_index:].lower().strip() 
            else:
                file_extension = None

            info_logger.info('Retrieved file extension {}'.format(file_extension))

            if file_extension in DOC_EXTENSIONS:
                # copy file to documents destination folder
                move_file(source_file_path, DEST_DIRS['dest_doc'], file_name)

            elif file_extension in MUS_EXTENSIONS:
                # copy file to music destination folder
                move_file(source_file_path, DEST_DIRS['dest_mus'], file_name)

            elif file_extension in IMG_EXTENSIONS:
                # copy file to images destination folder
                move_file(source_file_path, DEST_DIRS['dest_img'], file_name)

            elif file_extension in VID_EXTENSIONS:
                # copy file to videos destination folder
                move_file(source_file_path, DEST_DIRS['dest_vid'], file_name)

            else:
                # copy file without extension to unsorted folder
                move_file(source_file_path, DEST_DIRS['dest_unsorted'], file_name, False)

    except Exception:
        error_logger.error('Error in extract_file_extensions(files) method.')

    info_logger.info('End extract_file_extensions(files) function')


def move_file(source_file_path, destination_file_path, filename, is_extension = True):
    '''logging
        Function to move a file from a source directory 
        to a destination directory.

        @inputs:: 
                 source_file_path:str -> absolute source file path of file to move.
                 destination_file_path:str -> destination file path to move file to.
                 filename:str -> name of the file to be copied to destination.
                 is_extension:bool -> optional parameter flag used to indicate whether
                                      filename passed in has a valid extension checked for.
                                      Dafault value is True.
        @output:: none
    '''
    info_logger.info('Start move_file(...) function')
    info_logger.info('Moving file {}'.format(filename))

    # check if file already exists, if so add counter increment to the new file being 
    # copied to make it a unique filename.
    counter = 2

    try:
        # loop to generate a unique name of file being moved to destination if current
        # name of file already exists in destination directory.
        while True:
            info_logger.info('Generate unique file name to copy to destination directory.')

            # check if file exists before trying to copy file to destination
            if os.path.exists(destination_file_path + filename):

                if is_extension:
                    # slpit file name to append counter value to create a unique file name.
                    parts = filename.split('.')
                    filename = parts[0] + str(counter) + '.' + parts[1]

                else:
                    filename = filename + str(counter)

                # increment counter variable
                counter += 1
            else:
                break

        # move file to destination
        mv.move(source_file_path, destination_file_path + filename)

        info_logger.info('')
        info_logger.info('File {} successfully moved to {}'.format(filename, destination_file_path))
        info_logger.info('')

    except Exception as e:
        error_logger.error(f'Error moving file {filename} to destination {destination_file_path}.')
        error_logger.error(e)

    info_logger.info('End move_file(...) function')


class Watcher:

    try:

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
    except Exception as e:
        error_logger.error(e)
    

class MonitorDocumentCreation(FileSystemEventHandler):

    def on_created(self, event):
        info_logger.info('Initiate on_created event')

        # only process files, not directories
        if not event.is_directory:
            main()


if __name__ == "__main__":
    create_logging_directory()
    print('Created logging directory.')  

    configure_logging()
    info_logger.info('Configured logging and log level files.')

    create_destination_directories()
    info_logger.info('Created destination directories.')

    info_logger.info('Start create and run/start Watcher object.')
    download_watcher = Watcher(SOURCE_DIR, MonitorDocumentCreation())
    download_watcher.run()