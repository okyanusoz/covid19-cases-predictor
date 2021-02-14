"""
Predicts COVID-19 deaths.
Simply pass the path to the country data CSV file as an argument.
Can also be used programmatically.
Most of the code from https://github.com/anaiy2004/COVID-19-Forecasting.
Thank you so much Anaiy Somalwar!
"""
import csv
import keras
import pandas
from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate, BatchNormalization, Conv1D, Conv2D, Flatten, MaxPooling1D
from keras import optimizers
import numpy as np
import tensorflow as tf
import math
from keras.callbacks import EarlyStopping, ModelCheckpoint
from matplotlib import pyplot as plt
from sklearn.linear_model import RidgeCV
import sys

def predict_deaths(csv_file_path):
  df = pandas.read_csv(csv_file_path)
  inputs = df['cases'].to_numpy()
  outputs = df['deaths'].to_numpy()
  days = []
  count = 0
  for elements in inputs:
    count += 1
    days.append(count)
  df['days'] = days
  df.head()
  past = 5 
  s = (len(inputs) , past  * 2)
  betterinputs = np.zeros(s)
  betteroutputs = np.zeros(len(inputs))

  for i in range(len(inputs) - past ): #
    temp = np.zeros(past * 2)
    temp[0 : past] = inputs[i : i+ past]
    temp[past:] = outputs[i : i + past] 
    betterinputs[i] = temp
    betteroutputs[i] = outputs[i+past] #
  betterinputs = betterinputs[0:len(df)-past]  #
  betteroutputs = betteroutputs[0:len(df)-past] #
  days = days[0:len(df) - past]
  split = int(0.8*len(betterinputs))
  X_train, X_test, y_train, y_test = betterinputs[:split], betterinputs[split:], betteroutputs[:split], betteroutputs[split:]
  days = days[split:]
  X_train = np.expand_dims(X_train, axis=2)  
  X_test = np.expand_dims(X_test, axis=2)
  model = RidgeCV(cv=2)
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
  print(f"Prediction for tomorrow's deaths: {predict_deaths(sys.argv[1])}")