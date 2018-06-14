# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:42:04 2018

@author: Karan Sharma
"""

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("iris.csv")
X=dataset.iloc[:,0:4].values
y=dataset.iloc[:,-1].values

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

'''Output is in string format(categorical form) so doing Encoding of categorical data'''
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,y_train)
knn.predict([[5,1,5.0,0.6],[5,1,4.9,0.6]])
knn.predict(X_test)  
knn.predict([[5,3.4,1.6,0.4],[6.9,3.2,5.7,2.3]])

from sklearn.linear_model import LogisticRegression
logistic_regressor=LogisticRegression()
logistic_regressor.fit(X_train,y_train)
logistic_regressor.predict(X_test)
logistic_regressor.predict([[5,1,5.0,0.6],[5,1,4.9,0.6]])
logistic_regressor.predict([[5,3.4,1.6,0.4],[6.9,3.2,5.7,2.3]])


'''Histograms'''
dataset.hist()
plt.show()

from pandas.tools.plotting import scatter_matrix
'''Scatter matrix: n*n, n is name of columns/attribute'''
scatter_matrix(dataset)
plt.show()