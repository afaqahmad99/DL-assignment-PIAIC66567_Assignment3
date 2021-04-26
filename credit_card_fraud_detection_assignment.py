# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8bKdyvl4YFPjmA00vYBNJYNWV6tUYjn

# Credit Card Fraud Detection::
Download dataset from this link:

https://www.kaggle.com/mlg-ulb/creditcardfraud

# Description about dataset::
The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning.

Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.
# WORKFLOW :
1.Load Data

2.Check Missing Values ( If Exist ; Fill each record with mean of its feature )

3.Standardized the Input Variables.

4.Split into 50% Training(Samples,Labels) , 30% Test(Samples,Labels) and 20% Validation Data(Samples,Labels).

5.Model : input Layer (No. of features ), 3 hidden layers including 10,8,6 unit & Output Layer with activation function relu/tanh (check by experiment).

6.Compilation Step (Note : Its a Binary problem , select loss , metrics according to it)

7.Train the Model with Epochs (100).

8.If the model gets overfit tune your model by changing the units , No. of layers , epochs , add dropout layer or add Regularizer according to the need .

9.Prediction should be > 92% 10.Evaluation Step 11Prediction

# Task::
# Identify fraudulent credit card transactions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models,layers,optimizers,utils
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import io 
from google.colab import files
data = files.upload()
car = pd.read_csv(io.BytesIO(data['creditcard.csv']))

car.tail()

car.info()

x=car.drop("Class",axis=1).copy()
y=car["Class"].copy()

x

y

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=123)

scaler = StandardScaler()
scaler.fit(x_train)

x_train =pd.DataFrame(scaler.transform(x_train),columns=x_train.columns)
x_test=pd.DataFrame(scaler.transform(x_test),columns=x_test.columns)

part_x_train, x_val, part_y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=2)

model=models.Sequential()
model.add(layers.Dense(16,activation=tf.nn.relu,input_shape=(30,)))
model.add(layers.Dense(16,activation=tf.nn.relu))
model.add(layers.Dense(1,activation=tf.nn.sigmoid))
model.compile(optimizer="rmsprop",loss="binary_crossentropy",metrics=["acc"])

history=model.fit(part_x_train,part_y_train,epochs=100,batch_size=512,validation_data=(x_val,y_val))

model.evaluate(x_test,y_test)

model.predict(x_test).sum()




