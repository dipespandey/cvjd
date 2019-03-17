"""
jd_dataset.py
.................
Job Description dataset
This module creates a dataframe of keywords for 
the given job descriptions
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

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


