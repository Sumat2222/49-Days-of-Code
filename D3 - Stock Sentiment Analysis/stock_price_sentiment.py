
# Stock Sentiment Analysis using News Headlines

import pandas as pd

df = pd.read_csv('stock-data\Data.csv', encoding="ISO-8859-1")

df.head() 

# Label '0' - Stock price decreased, Label '1' - Stock price increased (for the specific company)

"""Dividing data into *train* and *test* datasets:"""

train = df[df['Date'] < '20150101']
test = df[df['Date'] > '20141231']

# Removing Punctuations from headlines

data = train.iloc[:,2:27]
data.replace("[^a-zA-Z]", " ", regex=True, inplace=True)

# Renaming column names

list1 = [str(i) for i in range(25)]
#new_index = [str(i) for i in list1]
data.columns = list1
data.head()

for j in list1:
    data[j] = data[j].str.lower()
data.head()

headlines = []
for row in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row, 0:25]))

headlines[0]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# Implement Bag Of Words
cv = CountVectorizer(ngram_range=(2,2))
train_data = cv.fit_transform(headlines)

# Implement RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=200, criterion='entropy')
rfc.fit(train_data, train['Label'])

# Predict for Test dataset (same)
test_transform = []
for row in range(0, len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row, 2:27]))

test_dataset = cv.transform(test_transform)
predictions = rfc.predict(test_dataset)

# Import library for checking accuracy

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

matrix = confusion_matrix(test['Label'], predictions)
print(matrix)

score = accuracy_score(test['Label'], predictions)
print("Accuracy =", round(score*100, 4),"%")

report = classification_report(test['Label'], predictions)
print(report)
