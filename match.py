'''
Module that does the matching
'''
from os import listdir
from os.path import isfile, join
from io import StringIO
import multiprocessing as mp
import pandas as pd
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.matcher import PhraseMatcher
from dataset.jd_dataset import preprocess
from cvjd.models import CV, Candidate
import matplotlib.pyplot as plt


def create_profile(text, candi_name):
    text = str(text)    
    # Create CV Dataset
    text = preprocess(text)
    text = ' '.join(text)
    # Create JD Dataset
    df_jd = pd.read_csv("/Users/dipespandey/professional/cvjd/dataset/latest.csv", index_col=False)
    total_dataset = {}
    for job in df_jd:
        total_dataset[job] = [nlp(text) for text in df_jd[job].dropna(axis=0)]
    
    matcher = PhraseMatcher(nlp.vocab)
    for job in total_dataset:
        matcher.add(job, None, *total_dataset[job])
    
    doc = nlp(text)
    
    d = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id] # get the unicode ID
        span = doc[start : end] # get the matched slice of the doc
        d.append((rule_id, span.text))
    keywords = "\n".join(f'{i[0]} {i[1]} ({j})' for i,j in Counter(d).items())

    # Convert string of keywords to df
    df = pd.read_csv(StringIO(keywords), names=['Keywords_List'])
    df1 = pd.DataFrame(df.Keywords_List.str.split(' ',1).tolist(),columns = ['Subject','Keyword'])
    df2 = pd.DataFrame(df1.Keyword.str.split('(',1).tolist(),columns = ['Keyword', 'Count'])
    df3 = pd.concat([df1['Subject'],df2['Keyword'], df2['Count']], axis = 1) 
    df3['Count'] = df3['Count'].apply(lambda x: x.rstrip(")"))
    name = pd.read_csv(StringIO(candi_name), names = ['Candidate Name'])
    dataf = pd.concat((name['Candidate Name'], df3['Subject'], df3['Keyword'], df3['Count']), axis=1)
    dataf['Candidate Name'].fillna(dataf['Candidate Name'].iloc[0], inplace = True)
    print(dataf.Subject)
    return dataf

def multi_run_wrapper(args):
    dataf = create_profile(*args)
    print(dataf.shape)
    return dataf
    
def multiprocess_run():
    pool = mp.Pool(processes=mp.cpu_count())
    all_maps = [(candi.cv.text_from_doc, candi.name) for candi in Candidate.objects.all()]
    new_datafs = pool.map(multi_run_wrapper, all_maps)
    return new_datafs

def single_process_run():
    final_db = pd.DataFrame()
    for candi in Candidate.objects.all():
        text = candi.cv.text_from_doc
        dat = create_profile(text, candi.name)
        final_db = final_db.append(dat)
        print(final_db)


def plot_keyword_counts(final_database):
    final_database2 = final_database['Keyword'].groupby([final_database['Candidate Name'], final_database['Subject']]).count().unstack()
    final_database2.reset_index(inplace = True)
    final_database2.fillna(0,inplace=True)
    new_data = final_database2.iloc[:,1:]
    new_data.index = final_database2['Candidate Name']
    new_data.to_csv('sample.csv')
    plt.rcParams.update({'font.size': 10})
    ax = new_data.plot.barh(title="Resume keywords by category", legend=False, figsize=(20,100), stacked=True)
    labels = []
    for j in new_data.columns:
        for i in new_data.index:
            label = str(j)+": " + str(new_data.loc[i][j])
            labels.append(label)
    patches = ax.patches
    for label, rect in zip(labels, patches):
        width = rect.get_width()
        if width > 0:
            x = rect.get_x()
            y = rect.get_y()
            height = rect.get_height()
            ax.text(x + width/2., y + height/2., label, ha='center', va='center')
    # plt.show()
    # plt.savefig('out.eps', format='eps', dpi=1000)


def create_score():
    df = pd.read_csv('/Users/dipespandey/professional/cvjd/sample.csv', index_col=False)
    final_db = []
    for i in range(df.shape[0]):
        score_dict = {}
        series = df.loc[i]
        max_score = max(series[1:])
        keys = df.loc[i].keys()
        candi = series['Candidate Name']
        for j in keys:
            if df.loc[i][j] == max_score:
                score_dict['candidate'] = candi
                score_dict['score'] = max_score
                score_dict['job'] = j 
                final_db.append(score_dict)
    return final_db
                
