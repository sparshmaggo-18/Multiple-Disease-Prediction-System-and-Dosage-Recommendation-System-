# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 03:40:27 2025

@author: SPARSH
"""

import numpy as np
import pickle

# loading the saved model
model=pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/breast_cancer_model.sav','rb'))

input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)

#change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 0):
  print('The Breast Cancer is Malignant')
else:
  print('The Breast Cancer is Benign')