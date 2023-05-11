#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:07:06 2023

This script reads a a modified version of the .csv produced by the function listing files.
The modified version should have a column named "Modified_Name" with new names of the file
names you want to substitute.

@author: vite
"""

import os
import csv
import sys

def modify_file_names(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            original_name = row["File_Name"]
            modified_name = row["Modified_Name"]
            file_path = row["File_Path"]
            
            if modified_name not in ["NA", "Na", "na", ""]:
                new_path = os.path.join(os.path.dirname(file_path), modified_name)
                os.rename(file_path, new_path)
                print(f"Renamed {file_path} to {new_path}")
    print("Finished renaming files.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]  # Get the CSV file from command line argument
        modify_file_names(csv_file)
    else:
        print("Please provide a CSV file as a command line argument.")
