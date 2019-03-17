"""
cv.py
This module contains all the cv related works
including parsing, cleansing, etc.
Objective is to get the keywords out of the CV
"""
import os
import re
import sys
import string
from tika import parser

def filter_cvs(cv_folder) -> list:
    """
    takes in the cv_folder 
    returns only the cv files (pdf, or docx, or ...)
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(cv_folder):
        files.extend(filenames)
    print(len(files))
    files_with_duplicates = []
    files_without_duplicates = []
    for i in files:
        f = i.split(".")
        if "CV" in i or "cv" in i:
            if not any(f[0] in j for j in files_without_duplicates):
                files_without_duplicates.append(os.getcwd() + "/all_candidates/" + i)
    print(len(files_without_duplicates))
    return files_without_duplicates


def parse_cv(file: str) -> str:
    """
    input: file name of CV (String)
    output: string representation of CV
    """
    text = ""
    try:
        file_data = parser.from_file(file)

        # Get files text content
        text = file_data["content"]
        print(text)
    except Exception as e:
        print(e)
    return text




