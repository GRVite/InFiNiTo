import os

def remove_files_with_strings(search_strings, search_directory):
    """
    Removes files from the search directory that contain any of the specified strings in their names.

    Parameters:
    - search_strings: List of strings to search in the names of files.
    - search_directory: Directory to search for and remove files.
    """
    # Count of removed files for feedback
    removed_files_count = 0

    # Loop through all files in the search directory
    for file_name in os.listdir(search_directory):
        # Check if the file name contains any of the search strings
        if any(search_string in file_name for search_string in search_strings):
            file_path = os.path.join(search_directory, file_name)
            # Remove the file
            os.remove(file_path)
            removed_files_count += 1
            print(f"Removed: {file_name}")

    print(f"Total removed files: {removed_files_count}")

# Example usage
search_strings = ['example1', '.5', 'sample']
search_directory = '/path/to/search/directory'  # Replace with your actual directory path

remove_files_with_strings(search_strings, search_directory)
