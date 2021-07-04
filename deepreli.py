import pickle
import re
from boilerpy3 import extractors

import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D, Dropout, BatchNormalization, Bidirectional


def createModel():
    model = load_model('model/new_model.h5')
    return model

@st.cache(suppress_st_warning=True)
def cleanText(txt):
    txt = re.sub('http\S+', '', txt)
    txt = txt.replace('!', '.')
    txt = txt.replace('?', '.')
    txt = txt.replace('-', ' ')
    txt = re.sub('[^\.a-zA-Z0-9 ]', '', txt)
    txt = txt.split('.')
    for i in range(len(txt)):
        txt[i] = ' '.join(w if not w.isdigit() else '' for w in txt[i].split(' '))
    txt = '.'.join(txt)
    txt = txt.replace('-', ' ')
    while('  ' in txt):
        txt = txt.replace('  ', ' ')
    return ' '.join([LEMMA.lemmatize(w) for w in txt.split(' ') if w not in STOPWORDS])


@st.cache(suppress_st_warning=True)
def split_into_sentences(text):
    alphabets = "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"

    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    if "u.s." in text:
        text = text.replace("u.s.", "united states")
    if "m.d" in text:
        text = text.replace("m.d", "m<prd>d<prd>")
    if "p.m." in text:
        text = text.replace("p.m.", "p<prd>m<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms+" "+starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" "+suffixes+"[.] "+starters, " \\1<stop> \\2", text)
    text = re.sub(" "+suffixes+"[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


def predict(txt):
    txt = TOKENIZER.texts_to_sequences(txt)
    txt = pad_sequences(txt, padding='post', maxlen=200)
    return np.mean(MODEL.predict(txt))


def getTextFromURL(url):
    extractor = extractors.ArticleExtractor()
    doc = extractor.get_doc_from_url(url)
    return (doc.title, doc.content)

# Global Vars

TOKENIZER = Tokenizer(num_words=20000, split=' ', oov_token='<unw>')
with open('./model/tokenizer.pickle', 'rb') as handle:
    TOKENIZER = pickle.load(handle)

LEMMA = None
with open('./model/lemma.pickle', 'rb') as handle:
    LEMMA = pickle.load(handle)

MODEL = createModel()

STOPWORDS = []
with open('./model/stopwords.txt', 'r') as f:
    STOPWORDS = set(f.read().split('\n'))