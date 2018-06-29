# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:23:54 2018

@author: Karan Sharma
"""


# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Sunday.csv', header=None)
dataset1 = pd.read_csv('Gender.csv', header=None)

transactions = []
for i in range(0, 7500):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
gender=[]
for i in range(0, 300):
    gender.append(str(dataset1.values[i]))

gender=gender*25

for i in range(0, 7500):
        transactions=[ i + gender for i in transactions]
