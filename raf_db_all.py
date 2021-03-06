# -*- coding: utf-8 -*-
"""Raf-DB ALL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ut28udL2vuhWnyPFbfAjyOg1MrYaUu6b
"""

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/My Drive/SOP_EmotionDetection/Code

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import scipy.io
dat = scipy.io.loadmat('DATA.mat')
data = dat.get("DATA")

np.save('DATA.npy',data)

X = np.load('DATA.npy')
X.shape

y = np.load('y.npy')

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

np.save('cm_all.npy',cm)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred, average='macro')
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

y1 = np.load('y_pred_base.npy')
y2 = np.load('y_pred_dlp.npy')
y3 = np.load('y_pred_hog.npy')
y4 = np.load('y_pred_gab.npy')
y1.shape

y_sample = np.zeros(989)
#y_sample = numpy.empty(989, dtype=object)
for i in range (0,988):
  if y1[i] == 1 or y2[i] == 1 or y3[i] == 1 or y4[i] == 1 :
    y_sample[i] = 1
  else:
    y_sample[i] = 0

type(y_sample)
y_sample.shape

cm1 = np.load('cm_base.npy')
cm2 = np.load('cm_dlp.npy')
cm3 = np.load('cm_gab.npy')
cm4 = np.load('cm_hog.npy')
cm_sample = cm1 + cm2 +cm3 + cm4
cm_sample

