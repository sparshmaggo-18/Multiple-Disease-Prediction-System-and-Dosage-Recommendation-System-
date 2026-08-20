# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 05:01:15 2025

@author: SPARSH
"""

#used for working with those numpy arrays
import numpy as np

#used for loading the saved model
import pickle

#used for deployment/creating web page
import streamlit as st

# loading the saved model
loaded_model=pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/heart_disease_model.sav','rb'))


#creating a function for prediction
def heart_disease_prediction(input_data):
    
    #numeric_cols=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    #for i, col in enumerate(numeric_cols):
     #   input_data[:,i] = np.array(input_data[:,i], dtype=np.float64)
        
     
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
      
      


def main():
    
    #giving a title
    st.title('Heart Disease Prediction Web App')
    
    #getting the input data from the user  
    age=st.text_input('Enter Age')
    sex=st.text_input('Enter Sex')
    cp=st.text_input('Chest Pain Value')
    trestbps=st.text_input('Resting Blood Pressure Value')
    chol=st.text_input('Cholestoral Value')
    fbs=st.text_input('Fasting Blood Sugar Value')
    restecg=st.text_input('Resting Electrocardiographic Value')
    thalach=st.text_input('Maximum Heart Rate Achieved Value')
    exang=st.text_input('Exercise Induced Angina Value')
    oldpeak=st.text_input('Oldpeak Value')
    slope=st.text_input('Slope Value')
    ca=st.text_input('CA Value')
    thal=st.text_input('thal Value')
    
    
    #code for Prediction
    diagnosis=''
    
    #creating a button for Prediction
    if st.button("Heart Disease Test Result"):
        diagnosis=heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)



if __name__=='__main__':
    main()  















      