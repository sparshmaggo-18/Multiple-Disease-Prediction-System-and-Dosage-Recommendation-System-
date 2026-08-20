# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 02:31:11 2025

@author: SPARSH
"""
#for loading models:
import pickle

#for deploying the models:
import streamlit as st

#for making the sidebar for navigate:
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model= pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/trained_model.sav','rb'))

breast_cancer_model= pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/breast_cancer_model.sav','rb'))

heart_disease_model= pickle.load(open('C:/Users/SPARSH/Desktop/Machine Learning Project/heart_disease_model.sav','rb'))


#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Breast Cancer Prediction',
                            'Heart Disease Prediction'],
                           
                           icons=['activity','person','heart'],
                           
                           default_index=0)
    
    
    
#diabetes prediction page
if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    #getting the input data from user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    
    with col2:   
        Glucose= st.text_input('Glucose Level')
        
    with col3:
        BloodPressure= st.text_input('BloodPressure Value')
        
    with col1:
        SkinThickness= st.text_input('SkinThickness Value')
        
    with col2:
        Insulin= st.text_input('Insulin Level')
        
    with col3:
        BMI= st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age= st.text_input('Age of the Person')
    
 
    
    #code for prediction
    diabetes_dignosis=''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if(diabetes_prediction[0]==1):
            diabetes_dignosis = 'The Person is Diabetic'
         
        else:
            diabetes_dignosis = 'The Person is not Diabetic'
    
    st.success(diabetes_dignosis)
    
 
    
 

#breast cancer prediction page
if(selected=='Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')    
    
    
    #getting the input data from user
    #columns for input fields
    col1, col2= st.columns(2)
    
    with col1:
        Radius_mean = st.text_input('Value of radius_mean')
        Perimeter_mean = st.text_input('Value of perimeter_mean')
        Smoothness_mean = st.text_input('Value of smoothness_mean')
        Concavity_mean = st.text_input('Value of concavity_mean')
        Symmetry_mean = st.text_input('Value of symmetry_mean')
        Radius_se = st.text_input('Value of radius_se')
        Perimeter_se = st.text_input('Value of perimeter_se')
        Smoothness_se = st.text_input('Value of smoothness_se')
        Concavity_se = st.text_input('Value of concavity_se')
        Symmetry_se = st.text_input('Value of symmetry_se')
        Radius_worst = st.text_input('Value of radius_worst')
        Perimeter_worst = st.text_input('Value of perimeter_worst')
        Smoothness_worst = st.text_input('Value of smoothness_worst')
        Concavity_worst = st.text_input('Value of concavity_worst')
        Symmetry_worst = st.text_input('Value of symmetry_worst')
        
    
    with col2:
        Texture_mean = st.text_input('Value of texture_mean')
        Area_mean = st.text_input('Value of area_mean')
        Compactness_mean = st.text_input('Value of compactness_mean')
        Concave_points_mean = st.text_input('Value of concave_points_mean')
        Fractal_dimension_mean = st.text_input('Value of fractal_dimension_mean')
        Texture_se = st.text_input('Value of texture_se')
        Area_se = st.text_input('Value of area_se')
        Compactness_se = st.text_input('Value of compactness_se')
        Concave_points_se = st.text_input('Value of concave_points_se')
        Fractal_dimension_se = st.text_input('Value of fractal_dimension_se')
        Texture_worst = st.text_input('Value of texture_worst')
        Area_worst = st.text_input('Value of area_worst')
        Compactness_worst = st.text_input('Value of compactness_worst')
        Concave_points_worst = st.text_input('Value of concave_points_worst')
        Fractal_dimension_worst = st.text_input('Value of fractal_dimension_worst')
 
  
  
    #code for prediction
    breast_cancer_dignosis=''
    
    #creating button for prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[Radius_mean, Texture_mean, Perimeter_mean, Area_mean, Smoothness_mean, Compactness_mean,
                                            Concavity_mean, Concave_points_mean, Symmetry_mean, Fractal_dimension_mean, Radius_se,
                                            Texture_se, Perimeter_se, Area_se, Smoothness_se, Compactness_se, Concavity_se, Concave_points_se,
                                            Symmetry_se, Fractal_dimension_se, Radius_worst, Texture_worst, Perimeter_worst, Area_worst,
                                            Smoothness_worst, Compactness_worst, Concavity_worst, Concave_points_worst, Symmetry_worst, Fractal_dimension_worst]])


        if(breast_cancer_prediction[0]==0):
            breast_cancer_dignosis = 'The Breast Cancer is Malignant'
            
        else:
            breast_cancer_dignosis = 'The Breast Cancer is Benign'


    st.success(breast_cancer_dignosis)





#heart disease prediction page
if(selected=='Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    
    #getting the input data from user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age=st.text_input('Enter Age')
        trestbps=st.text_input('Resting Blood Pressure Value')
        restecg=st.text_input('Resting Electrocardiographic Value')
        oldpeak=st.text_input('Oldpeak Value')
        thal=st.text_input('thal Value')
        
    with col2:
        sex=st.text_input('Enter Sex')
        chol=st.text_input('Cholestoral Value')
        thalach=st.text_input('Maximum Heart Rate Achieved Value')
        slope=st.text_input('Slope Value')
        
    with col3:
        cp=st.text_input('Chest Pain Value')
        fbs=st.text_input('Fasting Blood Sugar Value')
        exang=st.text_input('Exercise Induced Angina Value')
        ca=st.text_input('CA Value')
   
    
    #code for prediction
    heart_disease_dignosis=''
   
    #creating button for prediction
   
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    
        if (heart_disease_prediction[0]==0):
          print('The Person does not have a Heart Disease')

        else:
          print('The person has Heart Disease')
         
    
    
    st.success(heart_disease_dignosis) 
    
   
    
    
    
    
    
    
    
    


