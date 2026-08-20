# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 04:55:52 2025

@author: SPARSH
"""

import numpy as np
import pickle

# loading the saved model
loaded_model=pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/heart_disease_model.sav','rb'))

input_data = (54,1,0,122,286,0,0,116,1,3.2,1,2,2)

#change input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the nump array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('The Person does not have a Heart Disease')

else:
  print('The person has Heart Disease')