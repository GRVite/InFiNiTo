#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:06:10 2023

This script takes a directory as an input and creates a .csv with the names of the files existent in that directory.

@author: vite
"""

import os
import csv
import sys

def create_csv(directory, option='A'):
    if option == 'A':
        # Option A: List all files in the directory
        items = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    elif option == 'B':
        # Option C: List all files in the directory and subdirectories
        items = [os.path.join(root, f) for root, dirs, files in os.walk(directory) for f in files]
    elif option == 'C':
        # Option D: List all directories in the directory
        items = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    elif option == 'D':
        # Option E: List all directories in the directory and subdirectories
        items = [os.path.join(root, d) for root, dirs, files in os.walk(directory) for d in dirs]
    else:
        print("Invalid option. Please choose one of the following options: 'A', 'B', 'C' o 'D'.")
        return

    items = sorted(items)  # Sort items by name

    # Prepare data for csv
    data = [["Name", "Path"]]
    for item in items:
        data.append([os.path.basename(item), item])

    # Write data to csv
    with open(os.path.join(directory, 'list_files_or_directories.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file has been created for option '{option}' in directory: {directory}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        directory = sys.argv[1]  # Get the directory from command line argument
        option = sys.argv[2]  # Get the option from command line argument
        create_csv(directory, option)
    else:
        print("Please provide a directory and an option ('A', 'B', 'C' o 'D') as command line arguments.")
