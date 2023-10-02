#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 01:57:47 2023

@author: vite
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:47:23 2023

@author: vite
"""

import csv
import os
import shutil

def copy_specific_file(src, dst, filename):
    """
    This function copies a specific file from each sub-directory in the source
    directory to the corresponding sub-directory in the destination directory.

    Parameters:
    src (str): The path to the source directory.
    dst (str): The path to the destination directory.
    filename (str): The name of the file to be copied.

    Returns:
    None
    """
    for dirpath, dirnames, filenames in os.walk(src):
        # Check if the specific file exists in the current directory
        src_file_path = os.path.join(dirpath, filename)
        if os.path.exists(src_file_path):
            # Compute the destination file path
            dst_file_path = os.path.join(dst, os.path.relpath(dirpath, src), filename)
            # Ensure the destination directory exists
            os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
            # Copy the file
            shutil.copy(src_file_path, dst_file_path)
            
def find_missing_files(src, filename):
    """
    This function identifies sub-sub-folders where a specific file is missing
    and writes the paths of these folders to a CSV file.

    Parameters:
    src (str): The path to the source directory.
    filename (str): The name of the file to be checked.

    Returns:
    None
    """
    missing_file_folders = []  # List to store folders where file is missing

    for dirpath, dirnames, filenames in os.walk(src):
        # Check if the specific file is missing in the current directory
        src_file_path = os.path.join(dirpath, filename)
        if not os.path.exists(src_file_path):
            missing_file_folders.append(dirpath)

    # Write the paths of folders with missing file to a CSV file
    csv_file_path = os.path.join(src, 'missing_file_folders.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Folder Path'])  # Write header
        for folder in missing_file_folders:
            writer.writerow([folder])


# Define the name of the file to be copied
filename = 'metadata.txt'
# Define the source and destination directories
src = '/path/to/source/directory'
dst = '/path/to/destination/directory'

# Call the function to copy the specific file
copy_specific_file(src, dst, filename)

# Call the function to find missing files and create the CSV
find_missing_files(src, filename)


