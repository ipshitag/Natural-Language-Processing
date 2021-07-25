import re
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import multiprocessing
import pandas as pd
stopwords_list = stopwords.words("english")


df = pd.read_csv(' ')

def clean_data(text):
    text = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', '', text)
    text = re.sub(r'[\\/×\^\]\[÷]', '', text)
    return text
def change_lower(text):
    text = text.lower()
    return text

def remover(text):
    text_tokens = text.split(" ")
    final_list = [word for word in text_tokens if not word in stopwords_list]
    text = ' '.join(final_list)
    return text
  
  def get_w2vdf(df,col):
    w2v_df = pd.DataFrame(df[col]).values.tolist()
    for i in range(len(w2v_df)):
        w2v_df[i] = w2v_df[i][0].split(" ")
    return w2v_df
  
  
 def train_w2v(w2v_df):
    cores = multiprocessing.cpu_count()
    w2v_model = Word2Vec(min_count=4,
                         window=4,
                         vector_size=300, 
                         alpha=0.03, 
                         min_alpha=0.0007, 
                         sg = 1,
                         workers=cores-1)
    
    w2v_model.build_vocab(w2v_df, progress_per=10000)
    w2v_model.train(w2v_df, total_examples=w2v_model.corpus_count, epochs=100, report_delay=1)
    return w2v_model
  
df[[cols]] = df[[cols]].astype(str)
df[cols] = df[cols].apply(change_lower)
df[cols] = df[cols].apply(clean_data)
df[cols] = df[cols].apply(remover)

w2v_df = get_w2vdf(df,"Description")
w2v_model = train_w2v(w2v_df)
