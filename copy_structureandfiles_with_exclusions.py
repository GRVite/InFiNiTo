#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:23:58 2024

@author: vite
"""

import os
import shutil

def copy_structure_and_files(src, dst, exclude_file=None):
    """
    Copies the folder structure from src to dst and all .mat files found in src to the corresponding location in dst,
    excluding a specified file.
    
    :param src: Source directory path
    :param dst: Destination directory path
    :param exclude_file: Filename to exclude from copying
    """
    # Make sure the destination directory exists
    os.makedirs(dst, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Create each directory in the destination
        for dir in dirs:
            os.makedirs(os.path.join(dst, os.path.relpath(os.path.join(root, dir), src)), exist_ok=True)
        
        # Copy .mat files to the corresponding directory in the destination, excluding the specified file
        for file in files:
            if file.endswith('.mat') and file != exclude_file:
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst, os.path.relpath(src_file_path, src))
                shutil.copy2(src_file_path, dst_file_path)

# Replace these paths with your actual paths
source_directory = '/Volumes/Tetractys/Tetractys/'
destination_directory = '/Users/vite/navigation_system/Data/CellExplorerData/'
exclude_filename = 'rez2.mat'  # Filename to exclude

copy_structure_and_files(source_directory, destination_directory, exclude_filename)
