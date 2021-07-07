#libraries required

import pandas as pd
import numpy as np
import re
import unicodedata

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

from sklearn.feature_extraction.text import CountVectorizer

#loading small corpus
nlp = spacy.load('en_core_web_sm')

#reading data
df = pd.read_csv("sentisum-assessment-dataset.csv")
#some cleaning
df = df.drop(['Unnamed: 1'],axis=1)
#renaming
df.columns = ["document"]

#list of contractions and their related expansions (from web)
contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how does",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
" u ": " you ",
" ur ": " your ",
" n ": " and ",
"tbh":"to be honest" }

#functions

def get_avg_word_len(x):
    """Get the average word length from a given sentence
    param x(str): the sentence of whose word length is to be taken
    return leng(numeric): the average word length """

    words = x.split()
    word_len = 0
    for word in words:
        word_len = word_len + len(word)
    return word_len/len(words)

def feature_extract(df,d):
    """Adds new columns in the given df, from the existing data
    count: number of words in the document (df[d])
    char count: number of characters in df[d]
    avg word_len: the average number of characters in the df[d]
    stop_words_len: number of stopwords present
    numeric_count: number of numeric characters present
    upper_counts: number of words in CAPS LOCK
    
    param df(dataframe): dataframe on which manipulation is to be done
    param d(str): column name in which the reuired words are present"""
    
    df['count']=df[d].apply(lambda x: len(str(x).split()))
    df['char count']=df[d].apply(lambda x: len(x))
    df['avg word_len'] = df[d].apply(lambda x:get_avg_word_len(x))
    df['stop_words_len'] = df[d].apply(lambda x: len([t for t in x.split() if t in STOP_WORDS]))
    df['numeric_count'] = df[d].apply(lambda x:len([t for t in x.split()if t.isdigit()] ))
    df['upper_counts'] = df[d].apply(lambda x: len([t for t in x.split() if t.isupper() and len(x)>3]))


def expand(x):
    """Some of the words like 'i'll', are expanded to 'i will' for better text processing
    The list of contractions is taken from the internet
    
    param x(str): the sentence in which contractions are to be found and expansions are to be done
    
    return x(str): the expanded sentence"""
    if type(x)== str:
        for key in contractions:
            value = contractions[key]
            x = x.replace(key,value)
        return x
    else:
        return x

def remove_accented_chars(x):
    """The function changes the accented characters into their equivalent normal form,
    to do so, normalize function with 'NFKD' is used which replaces the compatibility characters into
    theri euivalent
    
    param x(str): the sentence in which accented characters are to be detected and removes
    return x(str): sentence with accented characters replaced by their equivalent"""
    
    x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return x


def make_to_base(x):
    """Converting the words to their base word and dictionary head word i.e to lemmatize
    param x(str): the sentence in which the words are to be converted (lemmatization)
    return x(str): the lemmatized sentence"""
    
    x_list = []
    doc = nlp(x)
    
    for token in doc:
        lemma = str(token.lemma_)
        if lemma == '-PRON-' or lemma == 'be':
            lemma = token.text
        x_list.append(lemma)
    return (" ".join(x_list))
    
def preprocess(df,d):
    """Preprocesses the given document by applying the following functionalities
    lower: lowers all the characters for uniformity
    expansion: expands words like i'll to i will for better text classification
    remove special characters: using regex, removes all the punctuations etc
    remove space: removes trailing spaces and extra spaces between words
    remove accented characters: change accented characters to its normal equivalent
    remove stop words: removes the stop words in the sentence
    lemmatization: changes the words to their base form"""
    df[d] = df[d].apply(lambda x: x.lower())
    df[d] = df[d].apply(expand)
    df[d] = df[d].apply(lambda x: re.sub('[^A-Z a-z 0-9-]+', '', x))
    df[d] = df[d].apply(lambda x: " ".join(x.split()))
    df[d] = df[d].apply(lambda x: remove_accented_chars(x))
    df[d] = df[d].apply(lambda x: " ".join([t for t in x.split() if t not in STOP_WORDS]))
    df[d] = df[d].apply(lambda x: make_to_base(x))

def get_bow(df,d):
    cv = CountVectorizer(ngram_range=(1,1))
    text_counts = cv.fit_transform(df[d])
    bow = pd.DataFrame(text_counts.toarray(), columns = cv.get_feature_names())
    return bow
