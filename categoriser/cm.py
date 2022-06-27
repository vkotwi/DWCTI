# https://stackabuse.com/text-classification-with-python-and-scikit-learn/
from pymongo import MongoClient

import numpy as np
#import pandas as pd
import json as json
import re
import pickle
import csv
import time

import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
# nltk.download('word net')

from sklearn.datasets import load_files
from sklearn.metrics import classification_report, multilabel_confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold 
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelEncoder


try:
    svc = pickle.load(open('trained_svc.pkl', 'rb'))
except:
    print("Requires trained model. Please run tc.py first")
    sys.exit()

client = MongoClient('mongodb://localhost:27017/')
db_dataset = client["DWProject"]["DW_dataset"]
db_raw = db_dataset.find({'english': True}, {'url': 1, 'data': 1, 'categories': 1, 'relevant': 1})


stemmer = WordNetLemmatizer()

y_raw = []
x_cleaned = []

# Preproccesing
for entry in db_raw:
    if entry["relevant"] == True:
        y_raw.append(entry["categories"])
    else:
        #y_raw.append(["other"])
        y_raw.append([])

     # Remove all the special characters
    entry = re.sub(r'\W', ' ', str(entry["data"]))
    
    # remove all single characters
    entry = re.sub(r'\s+[a-zA-Z]\s+', ' ', entry)
    
    # Remove single characters from the start
    entry = re.sub(r'\^[a-zA-Z]\s+', ' ', entry) 
    
    # Substituting multiple spaces with single space
    entry = re.sub(r'\s+', ' ', entry, flags=re.I)
    
    # Removing prefixed 'b'
    entry = re.sub(r'^b\s+', '', entry)
    
    # Converting to Lowercase
    entry = entry.lower()
    
    # Lemmatization
    entry = entry.split()

    entry = [stemmer.lemmatize(word) for word in entry]

    entry = ' '.join(entry)
        
    x_cleaned.append(entry)


# Binarises target labels for model
mlb = MultiLabelBinarizer()
y_binarised = mlb.fit_transform(y_raw)


tv = TfidfVectorizer(stop_words=stopwords.words('english'), max_df=0.7, min_df=1, max_features=3000)
x_vectorised = tv.fit_transform(x_cleaned)

x_train, x_test, y_train, y_test = train_test_split(x_vectorised, y_binarised, test_size=0.8, random_state=3)

svc = OneVsRestClassifier(SVC(kernel='linear', probability=True, C=1.0, max_iter=3000))
trained_svc = svc.fit(x_train, y_train)
cm = trained_svc.confusion_matrix(x_test, y_test)

print(cm)


