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
from cvjd.models import CV

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


class Rule():
    '''
    Rule class containing several rules to extract 
    several information from the CV
    '''
    def __init__(self, cv):
        self.cv = cv
    
    def get_candidate_name(self):
        cv_name = self.cv.name
        print(cv_name)
        name = cv_name.lower().split('cv')[0]
        full_name = name.split('_')
        full_name = full_name[0] + ' ' + full_name[1]
        candidate = self.cv.candidate_set.first()
        candidate.name = full_name
        candidate.save()
    
    def find_email(self, ):
        regex = r"\S+@\S+"
        cv = self.cv.name
        email = re.findall(regex, cv.text_from_doc)
        if email is not None:
            return email[0]
        return ''

            
    def find_phone(self, ):
        regex = r"\+?\d+(?:[- \)]+\d+)+"
        cv = self.cv.name
        phone = re.findall(regex, cv.text_from_doc)
        if phone is not None:
            return phone[0]
        return ''
    
    def find_experience_years(self,):
        raise NotImplementedError
    
    def find_education_terms(self, ):
        raise NotImplementedError
    
    def find_skills(self, ):
        raise NotImplementedError
    
    def __str__(self):
        return self.cv