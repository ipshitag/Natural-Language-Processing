# !pip install gensim
# !pip install python-Levenshtein

#import required packages
import gensim
import pandas as pd

#get the dataset
URL = 'http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Cell_Phones_and_Accessories_5.json.gz'
df = pd.read_json(URL, compression='gzip', lines=True)

#do preprocessing
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)

#initialize the model
model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4,
)

#build vocabulary
model.build_vocab(review_text, progress_per=1000)

#train the model
model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)

#save the model
model.save("./word2vec-amazon-cell-accessories-reviews-short.model")

#print similar words

print(model.wv.most_similar("bad"))

print(model.wv.most_similar("good"))

print(model.wv.most_similar("return"))
