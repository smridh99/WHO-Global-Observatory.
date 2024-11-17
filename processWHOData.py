#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
from pandas import Series, DataFrame

#load csv file
test = pd.read_csv("who.csv")
# print(test)
# Renamed unnamed columns to country and year
test.rename(columns ={'Unnamed: 0':'Country', 'Unnamed: 1': 'Year'}, inplace=True)
# Renamed Life expectancy columns
test.rename(columns ={'Life expectancy at birth (years)':'LE0','Life expectancy at birth (years).1':'LE0M','Life expectancy at birth (years).2':'LE0F','Life expectancy at age 60 (years)':'LE60','Life expectancy at age 60 (years).1':'LE60M','Life expectancy at age 60 (years).2':'LE60F'}, inplace=True)
# Renamed HALE columns
test.rename(columns ={'Healthy life expectancy (HALE) at birth (years)': 'HALE0','Healthy life expectancy (HALE) at birth (years).1': 'HALE0M','Healthy life expectancy (HALE) at birth (years).2':'HALE0F','Healthy life expectancy (HALE) at age 60 (years)':'HALE60','Healthy life expectancy (HALE) at age 60 (years).1':'HALE60M','Healthy life expectancy (HALE) at age 60 (years).2':'HALE60F'}, inplace=True)
# Dropping unwanted headers
test = test.iloc[1: , :]

# Filling NaN with 0
# test = test.fillna(0)

# print(test.head())
test[['Year','LE0','LE0M','LE0F','LE60','LE60M','LE60F','HALE0','HALE0M','HALE0F','HALE60','HALE60M','HALE60F']] = test[['Year','LE0','LE0M','LE0F','LE60','LE60M','LE60F','HALE0','HALE0M','HALE0F','HALE60','HALE60M','HALE60F']].apply(pd.to_numeric)

#print(test.dtypes)

# Pickle the dataframe into the file
test.to_pickle("assignment2.pkl")


## Question 6 onwards: New Dataframe

newdf = test.pivot(index='Country', columns='Year', values='LE0')


# Adding mean to the column
newdf['Mean'] = newdf.mean(axis=1, skipna = True)
newdf['Max'] = newdf.max(axis=1)
newdf['Min'] = newdf.min(axis=1)
## FOR SD, we narrow down the columns
exc = newdf.loc[:, ~newdf.columns.isin(['Mean', 'Max','Min'])]
newdf['Std'] = exc.std(axis=1, skipna = True)

#Sorting the rows by mean in descending order
newdf = newdf.sort_values(by=['Mean'], ascending=False)

# print(newdf)

# Pickle the dataframe into the file
newdf.to_pickle("assignment2-le0.pkl")

# Question 7: HALE data

df2 = test.pivot(index='Country', columns='Year', values='HALE0')

df2 = df2.interpolate(axis=1)

#Summarize the data 
df2['Mean'] = df2.mean(axis=1, skipna = True)
df2['Max'] = df2.max(axis=1, skipna = True)
df2['Min'] = df2.min(axis=1, skipna = True)
## FOR SD, we narrow down the columns
exc1 = df2.loc[:, ~df2.columns.isin(['Mean', 'Max','Min'])]
df2['Std'] = exc1.std(axis=1, skipna = True)


df2 = df2.sort_values(by=['Mean'], ascending=False)
# print(df2.head())

#Save the dataframe to pickle
df2.to_pickle('assignment2-hale0.pkl')



# In[ ]:





# In[ ]:




