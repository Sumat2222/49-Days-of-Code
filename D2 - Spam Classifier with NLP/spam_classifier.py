# -*- coding: utf-8 -*-
"""spam-classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtDEO73FiN14-ekgHJPTybKaCmGD-Iqc

## Spam Classifier using NLP and ML Techniques

Dataset imported from: https://archive.ics.uci.edu/ml/datasets/sms+spam+collection#

Importing the dataset:
"""

import pandas as pd

messages = pd.read_csv('smsspamcollection\SMSSpamCollection.txt', sep='\t', names=["label", "message"])

"""### Data Cleaning and Processing:"""

import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
lemm = WordNetLemmatizer()
corpus = []

for i in range(len(messages)):
    review = re.sub('^a-zA-Z', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [lemm.lemmatize(word) for word in review if word not in stopwords.words('english')]   #Line comprehension for stemming
    review = ' '.join(review)
    corpus.append(review)

"""### Creating the Bag Of Words Model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
x = cv.fit_transform(corpus).toarray()

x.shape

y = pd.get_dummies(messages['label'])   #Divides into 2 categorical variables
y = y.iloc[:,1].values   #But we only need one category to represent 0,1 for ham, spam

"""Train Test Split:"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state = 0)

"""### Training model using MultinomialNB Classifier"""

from sklearn.naive_bayes import MultinomialNB
spam_detection_model = MultinomialNB().fit(x_train, y_train)

y_pred = spam_detection_model.predict(x_test)

"""Confusion Matrix for data comparison:"""

from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(y_test, y_pred)
confusion_m

"""Checking Accuracy:"""

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy = {}%".format(accuracy*100))