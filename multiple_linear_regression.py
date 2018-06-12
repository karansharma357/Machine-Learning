# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:08:57 2018

@author: Karan Sharma
"""

# Multiple Linear Regression

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#testing
plt.scatter(X_test[:,2], y_test, color = 'red')
plt.plot(X_test[:,2], y_pred, color = 'blue')
plt.title('Profit calculator w.r.t R&D Spend')
plt.xlabel('Money Spent in R&D')
plt.ylabel('Profit')
plt.show()


#training
plt.scatter(X[:,2], y, color = 'red')
plt.plot(X[:,2], regressor.predict(X), color = 'blue')
plt.title('Profit calculator w.r.t R&D Spend')
plt.xlabel('Money Spent')
plt.ylabel('Profit')
plt.show()

plt.scatter(X[:,3], y, color = 'red')
plt.plot(X[:,3], regressor.predict(X), color = 'blue')
plt.title('Profit calculator w.r.t Administration')
plt.xlabel('Money Spent')
plt.ylabel('Profit')
plt.show()

plt.scatter(X[:,4], y, color = 'red')
plt.plot(X[:,4], regressor.predict(X), color = 'blue')
plt.title('Profit calculator w.r.t Marketing Spend')
plt.xlabel('Money Spent')
plt.ylabel('Profit')
plt.show()
