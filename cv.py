"""
cv.py
This module contains all the cv related works
including parsing, cleansing, etc.
Objective is to get the keywords out of the CV
"""
import os
import re
import sys
import nltk
import string
from tika import parser
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmter
from nltk.stem.wordnet import WordNetLemmatizer


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


def clean_text(text: str) -> list:
    """
    input: raw text
    output: cleansed text
    """
    # split into words
    tokens = nltk.word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuations from each word
    table = string.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphanum
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if not w in stop_words]
    return words


def preprocess(text):
    stop_words = set(stopwords.words("english"))

    new_words = []
    stop_words = stop_words.union(new_words)

    # Remove punctuations
    text = re.sub("[^a-zA-Z]", " ", text)

    # Convert to lowercase
    text = text.lower()

    # Remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # Convert to list from string
    text = text.split()

    # Lemmatization
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if not word in stopwords]
    text = " ".join(text)
    return text
    

