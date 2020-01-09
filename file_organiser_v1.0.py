import os, shutil

# TODO : 1.Expand Dictioanry (might be a good idea to webscrape Wikipedia)
# TODO : 2.Add pyinputplus functionality for entering a valid inputFilepath() ! can check if file/folder exists


# Sample dict for extensions
file_types = {
    'Images': ['.jpeg', 'jpg', '.gif'],
    'Documents': ['.docx', '.pdf', '.doc', '.txt'],
    'Executables': ['.exe', '.msi'],
    'Python Files': ['.py'],
    'Uncategorized': ['.epub'],
    'APK Files': ['.apk'],
    'Subtitles': ['.srt'],
    'Zipped Files': ['.rar', '.zip', '.7zip'],
}

# Add the folder you want organised
###############################################
downloads_path = 'c:\\users\\ghira\\downloads'
###############################################

# Changing the directory to our downloads folder.
def set_downloads_folder(downloads_path):
    print(f'\nSelected Folder: {downloads_path}')
    print("Changing directory to -->", os.getcwd(), "\n")
    return os.chdir(downloads_path)


def get_my_files():
    """Getting just the files from our downloads folder."""
    return [file for file in os.listdir(os.getcwd()) if os.path.isfile(file)]


def get_file_extensions():
    """Getting each extension of our files."""
    my_files_ext = []
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file):
            file_info = os.path.splitext(file)
            file_ext = file_info[1]
            my_files_ext.append(file_ext)
    return [file for file in my_files_ext]


def check_same_files_ext(my_files, my_files_ext):
    if len(my_files_ext) != len(my_files):
        raise Exception('Files lenght not equal to extension lenght\nExiting...')


def info_print(my_files, my_files_ext):
    """Prints information"""
    my_files_lenght = len(my_files)
    ext_lenght = len(my_files_ext)
    print(f'Files({my_files_lenght}) :{my_files}')
    print(f'Extensions({ext_lenght}) :{my_files_ext}\n')


def create_folders(folder_name):
    """Creates appropriate folders if needed"""

    if os.path.exists(downloads_path + '\\' + folder_name):
        pass
    else:
        os.makedirs(folder_name)
        print(f'Folder: {folder_name} has been created in {downloads_path}')


def check_and_move_files(my_files, my_files_ext):
    """Checks to see if the extensions of our current files are
    in the dictionary if so, it moves them to the according folder"""
    for key, value in file_types.items():
        for filename, ext in zip(my_files, my_files_ext):
            if ext in value:
                # print(downloads_path + '\\' + filename)
                folder_name = key
                create_folders(folder_name)
                shutil.move(downloads_path + '\\' + filename, downloads_path + '\\' + folder_name + '\\' + filename)
                print(f'File: {filename} moved to folder: {folder_name}')


def move_unmoved_to_uncategorized():
    files_not_moved = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file)]
    print(f'\nUncategorized files : {[file for file in files_not_moved]}')
    folder_name = 'Uncategorized'
    for file in files_not_moved:
        shutil.move(downloads_path + '\\' + file, downloads_path + '\\' + folder_name + '\\' + file)
    print(f'Moving uncategorized files to : {folder_name} folder')


if __name__ == '__main__':
    set_downloads_folder(downloads_path)
    my_files = get_my_files()
    my_files_ext = get_file_extensions()
    check_same_files_ext(my_files, my_files_ext)
    info_print(my_files, my_files_ext)
    check_and_move_files(my_files, my_files_ext)
    move_unmoved_to_uncategorized()