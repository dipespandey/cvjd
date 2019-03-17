"""
jd_dataset.py
.................
Job Description dataset
This module creates a dataframe of keywords for 
the given job descriptions
"""
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmter
from nltk.stem.wordnet import WordNetLemmatizer


def read_dataset(dataset) -> DataFrame:
    '''
    read the csv/xlsx file and return the not null cols version of DF
    '''
    df = pd.read_csv(dataset)
    null_cols = df.columns[df.isnull().any()] 
    not_null_cols = df.columns.difference(null_cols)
    return df[not_null_cols]


def create_keywords(df: DataFrame, text:str) -> list:
    '''
    take in a text and return the list of important keywords
    assign the list to columns in the DF
    '''
    keywords = []
    df_n = pd.DataFrame(columns = df.columns)
    for i in df_n:
        df_n[i] = pd.Series(keywords)
    return df_n



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


