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

def create_csv(directory):
    # List all files in directory
    all_files = os.listdir(directory)

    # Prepare data for csv
    data = [["File_Name", "File_Path"]]
    for file_name in all_files:
        data.append([file_name, os.path.join(directory, file_name)])

    # Write data to csv
    with open('files.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file has been created for all files in directory: {directory}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]  # Get the directory from command line argument
        create_csv(directory)
    else:
        print("Please provide a directory as a command line argument.")
