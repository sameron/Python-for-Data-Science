# Python program that locates the different file names and types located in a directory:
import time

def get_file_extension(file: str, *args) -> any:
    # Find the index of the last '.' in the string
    dot_index = file.rfind('.')
    if dot_index == -1:
        # No '.' was found, so return an empty string
        return None
    else:
        # Return the portion of the string after the last '.'
        return file[dot_index+1:]


def get_dir_details_with_os(path: str) -> None:
    import os
    # Specify the directory to search
    # directory = '/path/to/directory/*'
    directory = path

    # Get a list of all files in the directory
    files = os.listdir(directory)

    for file in files:
        if get_file_extension(file) is not None or '.' in file:
            print(file, " ", get_file_extension(file))
        else:
            print(file)


def get_dir_details_with_glob(path: str) -> None:
    import os
    import glob

    # Specify the directory to search
    directory = '{}\\*'.format(path)
    # Get a list of all files in the directory
    files = glob.glob(directory)

    # Print the names and types of all files in the directory
    for file in files:
        file_type = get_file_extension(file)
        if file_type is not None:
            print(f"{file} \t {file_type}")


def get_dir(path: str) -> None:
    import os

    # Specify the directory to search
    directory = path

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Get a set of all file types in the directory
    file_types = set()
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            file_type = 'directory'
        else:
            file_type = os.path.splitext(file)[1]
        file_types.add(file_type)

    # Print the file types
    print("File types in {}:".format(directory), file_types)


# Testing the functions
get_dir_details_with_os('C:\\Users\\HP\\Desktop')
time.sleep(2)
get_dir_details_with_glob('C:\\Users\\HP\\Desktop')
time.sleep(2)
get_dir('C:\\Users\\HP\\Desktop')
