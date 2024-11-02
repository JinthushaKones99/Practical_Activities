# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kVlVT384vC29Bv4xRmuRpuK4kvlwcFYs
"""

#imporint libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

#Load dataset
df_titanic=pd.read_csv('/content/sample_data/Titanic-Dataset.csv')

#Explore data
print("Shape of the dataset", df_titanic.shape)
print("\nColumn names and their data types",df_titanic.dtypes)
print("\nNull Values", df_titanic.isnull().sum())
print("\nduplicate values", df_titanic.duplicated().sum())
print("\nStatistics", df_titanic.describe())

#Handling Missing values
imputer=SimpleImputer(strategy='median')
df_titanic['Age']=imputer.fit_transform(df_titanic[['Age']])


df_titanic.fillna({'Embarked':df_titanic['Embarked'].mode()[0]}, inplace=True)

df_titanic.drop(columns=['Cabin'], inplace=True)

print(df_titanic.head)

#Encoding
encoder=LabelEncoder()
df_titanic['Sex']=encoder.fit_transform(df_titanic['Sex'])
df_titanic['Embarked']=encoder.fit_transform(df_titanic['Embarked'])

print(df_titanic.head)

#scaling
scaler=MinMaxScaler()
df_titanic_scaled=scaler.fit_transform(df_titanic[['Age','Sex','Embarked']])

print(df_titanic)

#PCA
pca=PCA(n_components=2)
df_titanic_pca=pca.fit_transform(df_titanic_scaled)

print(df_titanic_pca)