"""
Predicts COVID-19 cases.
Simply pass the path to the country data CSV file as an argument.
Can also be used programmatically.
Most of the code from https://github.com/anaiy2004/COVID-19-Forecasting.
Thank you so much Anaiy Somalwar!
"""
import keras
import pandas
import numpy as np
import math
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
import sys

def predict_cases(csv_file_path):
  df = pandas.read_csv(csv_file_path)
  inputs = df['cases'].to_numpy()
  outputs = df['deaths'].to_numpy()
  df.tail(5)
  days = []
  count = 0
  for elements in inputs:
    count += 1
    days.append(count)
  df['days'] = days
  past = 7
  s = (len(inputs) , past  * 2)
  betterinputs = np.zeros(s)
  betteroutputs = np.zeros(len(inputs))

  for i in range(len(inputs) - past): # - 0
    temp = np.zeros(past * 2)
    temp[0 : past] = inputs[i : i+ past]
    temp[past:] = outputs[i : i + past] 
    betterinputs[i] = temp
    betteroutputs[i] = inputs[i+past] # + 0
  betterinputs = betterinputs[0:len(df) - past] # - 0
  betteroutputs = betteroutputs[0:len(df) - past]
  days = days[0:len(df) - past]
  split = int(0.8*len(betterinputs))
  X_train, X_test, y_train, y_test = betterinputs[:split], betterinputs[split:], betteroutputs[:split], betteroutputs[split:]
  X_train = np.expand_dims(X_train, axis=2)  
  X_test = np.expand_dims(X_test, axis=2) 
  days = days[split:]
  model = RidgeCV(cv = 2)
  X_train, X_test, y_train, y_test = betterinputs[:split], betterinputs[split:], betteroutputs[:split], betteroutputs[split:]
  model.fit(X_train, y_train)

  size = (2 , past  * 2)
  finalInput = np.zeros(size)
  temp = np.zeros(past * 2)
  temp[:past] = inputs[-past:]
  temp[past:] = outputs[-past:] 
  finalInput[0] = temp
  finalInput[1] = temp

  futurePrediction = model.predict(finalInput)
  futurePrediction = futurePrediction[0]
  return int(futurePrediction)

if(__name__  == "__main__"):
  print(f"Prediction for tomorrow's cases: {predict_cases(sys.argv[1])}")
