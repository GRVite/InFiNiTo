#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:55:38 2023

Inputs:
    directory: str
    keyword: str

Outputs:
    matching_files: list
        -It contains all the files in a given directory that match a given keyword
        
@author: vite
"""

import os
import fnmatch

def find_files(directory, keyword):
    matching_files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, f"*{keyword}*"):
            matching_files.append(os.path.join(root, filename))
    return matching_files