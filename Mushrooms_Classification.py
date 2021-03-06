# -*- coding: utf-8 -*-
"""Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y5RPbqVlfKQM2Ykt12jM0Fgk_iNzG39c
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# getting dataset

df = pd.read_csv("/content/mushrooms.csv")

df.shape

df.head()

le = LabelEncoder()

df_encoded = df.apply(le.fit_transform, axis=0)

df_encoded.head()

df = df_encoded.values

X = df[: ,1:]
X

y = df[: ,0]
y

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

"""# Posterior Probability
  ##Likelyhood
  ##Prior Probability
"""

# Prior Probability

def prior_probab(y_train, label):
  m = y_train.shape[0]
  s = np.sum(y_train == label)
  return m/s

def cond_probab(X_train, y_train, feature_col, feature_val, label):
  X_filtered = X_train[y_train == label]
  num = np.sum(X_filtered[:, feature_col] == feature_val)

  denom = X_filtered.shape[0]

  return float(num/denom)

def predict(X_train, y_train, X_test):
  classes = np.unique(y_train)
  n_features = X_train.shape[1]
  posterior_probab = []

  for label in classes:
    likelyhood = 1.0
    for fea in range(n_features):
      cond = cond_probab(X_train, y_train, fea, X_test[fea], label)
      likelyhood = likelyhood * cond
    prior = prior_probab(y_train, label)
    post = likelyhood * prior

    posterior_probab.append(post)

    pred = np.argmax(posterior_probab)

    return pred

def accuracy(X_train, y_train, X_test, y_test):
  pred = []

  for i in range(X_test.shape[0]):
    p = predict(X_train, y_train, X_test[i])
    pred.append(p)
  
  y_pred = np.array(pred)
  acc = np.sum(y_pred == y_test) / y_pred.shape[0]

  return acc

acc = accuracy(X_train, y_train, X_test, y_test)

acc*100

