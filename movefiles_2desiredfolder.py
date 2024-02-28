import os
import shutil

def move_files_to_folder(search_directory, folder_name, search_string):
    # Create the full path for the new folder within the search directory
    new_folder_path = os.path.join(search_directory, folder_name)

    # Check if the folder exists, if not, create it
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created in {search_directory}")

    # Loop through all files in the search directory
    for file_name in os.listdir(search_directory):
        # Check if the file name contains the search string
        if search_string in file_name:
            # Create the full path for the source and destination
            src_path = os.path.join(search_directory, file_name)
            dest_path = os.path.join(new_folder_path, file_name)

            # Move the file to the new folder
            shutil.move(src_path, dest_path)
            print(f"Moved: {file_name}")

# Example usage
search_directory = '/path/to/search/directory'  # Update this path to your specific directory
folder_name = 'new_folder'
search_string = '.5'
move_files_to_folder(search_directory, folder_name, search_string)
