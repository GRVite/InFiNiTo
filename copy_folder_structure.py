#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:47:23 2023

@author: vite
"""

import os

def copy_structure(src, dst):
    """
    This function replicates the directory structure of the source directory
    to the destination directory without copying the files contained within
    the directories.

    Parameters:
    src (str): The path to the source directory whose structure is to be copied.
    dst (str): The path to the destination directory where the structure is to be replicated.

    Returns:
    None
    """
    for dirpath, dirnames, filenames in os.walk(src):
        # Compute the destination directory path
        dst_dir = os.path.join(dst, os.path.relpath(dirpath, src))
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

# Define the source and destination directories
src = '/path/to/source/directory'
dst = '/path/to/destination/directory'

# Call the function to copy the directory structure
copy_structure(src, dst)
