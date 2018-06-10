# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:59:28 2018

@author: Karan Sharma
"""

import pandas as pd
dataset=pd.read_csv('Data.csv')

#create an array
arr=[]
for i in range(1,11):
    arr.append(i*1)
    
#creating/inserting a new column in dataset 
dataset.insert(2,'Sales',arr,allow_duplicates=False)

