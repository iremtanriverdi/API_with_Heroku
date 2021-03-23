# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


dataset = pd.read_csv('kc_house_data.csv')

X = dataset.iloc[:, [3,4,7,8,9,10,11]] # seleceting covariates from dataset
y = dataset.iloc[:, 2] # seleceting response from dataset

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 2, 2,1,2,3,6]]))


