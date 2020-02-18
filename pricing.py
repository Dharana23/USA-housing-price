# -*- coding: utf-8 -*-
"""Pricing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nOEzcjEVBVBMcEkKd27mmeaZ1SWzPZ1O
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('user uploaded file "{name}" with length "{length}" bytes'.format(name = fn, length = len(uploaded[fn])))

uploaded

import io

df = pd.read_csv(io.StringIO(uploaded['USA_Housing.csv'].decode('utf-8')))

df.head()

df.info()

df.describe()

df.columns

sns.pairplot(df)

sns.distplot(df['Price'])

sns.heatmap(df.corr(), annot=True)

df.columns

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address']]

y = df['Price']

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

X = X.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')

X.fillna(0, inplace=True)
y.fillna(0, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.4, random_state=101)
clf = LinearRegression().fit(X_train, y_train)

clf

print(clf.intercept_)

clf.coef_

lm = pd.DataFrame(clf.coef_, X.columns, columns=['coeff'])

lm

predictions = clf.predict(X_test)

plt.scatter(y_test, predictions)

sns.distplot((y_test-predictions))

from sklearn import metrics

metrics.mean_absolute_error(y_test, predictions)

metrics.mean_squared_error(y_test, predictions)

np.sqrt(metrics.mean_squared_error(y_test, predictions))

