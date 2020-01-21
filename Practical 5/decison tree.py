#!/usr/bin/env python
# coding: utf-8

# In[119]:


#import statement
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#import a dataset from sklearn
from sklearn.datasets import load_breast_cancer
#id3
from id3 import Id3Estimator
from id3 import export_graphviz
import pydotplus
from IPython.display import Image  
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn import preprocessing
from IPython.display import SVG
from graphviz import Source


# In[118]:


#import data from csv file 
weather_data = pd.read_csv('weather.csv')
#print(data)


# In[76]:


weather_data.columns


# In[121]:


import csv

with open('weather.csv', newline='') as f:
    reader = csv.reader(f)
    weather_data = list(reader)

target =[]
for row in weather_data:
    target.append(row[4])
    del(row[4])
       
target.remove(target[0])
print(weather_data.remove(weather_data[0]))
weather_data
#target


# In[124]:


le = preprocessing.LabelEncoder()
data = []
for i in range(0,14):
    le.fit(weather_data[i])
    data.append(le.transform(weather_data[i]))

target =[1,1,1,1,1,1,0,1,0,0,0,0,1,1]


# In[135]:


data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(data,target)
clf.predict([[3, 2, 1, 0]])


# In[131]:


print(data)


# In[ ]:




