pip install transformers==3.5.1
from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained('bert-base-uncased')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = 'I love India'

tokens = tokenizer.tokenize(sentence)

print(tokens)
