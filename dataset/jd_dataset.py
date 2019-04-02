"""
jd_dataset.py
.................
Job Description dataset
This module creates a dataframe of keywords for 
the given job descriptions
"""
import sys
import re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from pandas import DataFrame

import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


def read_dataset(dataset) -> DataFrame:
    """
    read the csv/xlsx file and return the not null cols version of DF
    """
    df = pd.read_csv(dataset, index_col=None)
    null_cols = df.columns[df.isnull().any()]
    not_null_cols = df.columns.difference(null_cols)
    return df[not_null_cols]


def create_keywords(df: DataFrame) -> DataFrame:
    """
    take in a text and get the list of important keywords
    assign the list to columns in the DF
    """
    df_n = pd.DataFrame(columns=df.columns)
    for i in df_n:
        list_title = i.lower().split('_')
        list_title = list_title * 10
        keywords = preprocess(df[i][0])
        df_n[i] = pd.Series(keywords+list_title)
    return df_n


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def preprocess(text):
    stop_words = set(stopwords.words("english"))

    new_words = ['also', 'based', 'new', 'great', 'similar', 'run', 'role', 'day', 'working', 'always',
                 'must', 'may', 'along', 'held', 'well', 'lot', 'special',
                 'similar', 'often', 'high', 'entire', 'main', 'preparing', 'etc', 'keep', 'time', 'small', 'take', 'takes', 'regardless', 'able', 
                 'take', 'likely', 'responsible', 'importantly', 'advanced', 'run' , 'work', 'everything', 'list', 'find', 'assumes', 'important', 
                 'could', 'ensure', 'highly', 'undertakes']

    stop_words = stop_words.union(new_words)

    # Remove punctuations
    # text = re.sub("[^a-zA-Z0-9]", " ", str(text))

    # Convert to lowercase
    text = text.lower()

    # Convert to list from string
    text = nltk.word_tokenize(text)

    # Lemmatization
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word, get_wordnet_pos(word)) for word in text if not word in stop_words]
    # print(text)
    # text = " ".join(text)
    return text


def full_run():
    dataset = '/Users/dipespandey/professional/cvjd/dataset/crew_jd.csv'
    df = read_dataset(dataset)
    df_n = create_keywords(df)
    df_n.to_csv('/Users/dipespandey/professional/cvjd/dataset/latest_jd.csv', index=None)