# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:37:07 2025

@author: SPARSH
"""

# used for working with those numpy arrays
import numpy as np

# used for loading the saved model
import pickle

# used for deployment/creating web page
import streamlit as st


# loading the saved model
model = pickle.load(open(
    'C:/Users/SPARSH/Desktop/Machine Learning Project/breast_cancer_model.sav', 'rb'))

# creating a function for prediction

def breast_cancer_prediction(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return ('The Breast Cancer is Malignant')
    else:
        return ('The Breast Cancer is Benign')


def main():

    # giving a title
    st.title('Breast Cancer Prediction Web App')

    # getting the input data from the user
    Radius_mean = st.text_input('Value of radius_mean')
    Texture_mean = st.text_input('Value of texture_mean')
    Perimeter_mean = st.text_input('Value of perimeter_mean')
    Area_mean = st.text_input('Value of area_mean')
    Smoothness_mean = st.text_input('Value of smoothness_mean')
    Compactness_mean = st.text_input('Value of compactness_mean')
    Concavity_mean = st.text_input('Value of concavity_mean')
    Concave_points_mean = st.text_input('Value of concave_points_mean')
    Symmetry_mean = st.text_input('Value of symmetry_mean')
    Fractal_dimension_mean = st.text_input('Value of fractal_dimension_mean')
    Radius_se = st.text_input('Value of radius_se')
    Texture_se = st.text_input('Value of texture_se')
    Perimeter_se = st.text_input('Value of perimeter_se')
    Area_se = st.text_input('Value of area_se')
    Smoothness_se = st.text_input('Value of smoothness_se')
    Compactness_se = st.text_input('Value of compactness_se')
    Concavity_se = st.text_input('Value of concavity_se')
    Concave_points_se = st.text_input('Value of concave_points_se')
    Symmetry_se = st.text_input('Value of symmetry_se')
    Fractal_dimension_se = st.text_input('Value of fractal_dimension_se')
    Radius_worst = st.text_input('Value of radius_worst')
    Texture_worst = st.text_input('Value of texture_worst')
    Perimeter_worst = st.text_input('Value of perimeter_worst')
    Area_worst = st.text_input('Value of area_worst')
    Smoothness_worst = st.text_input('Value of smoothness_worst')
    Compactness_worst = st.text_input('Value of compactness_worst')
    Concavity_worst = st.text_input('Value of concavity_worst')
    Concave_points_worst = st.text_input('Value of concave_points_worst')
    Symmetry_worst = st.text_input('Value of symmetry_worst')
    Fractal_dimension_worst = st.text_input('Value of fractal_dimension_worst')

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        diagnosis = breast_cancer_prediction([Radius_mean, Texture_mean, Perimeter_mean, Area_mean, Smoothness_mean, Compactness_mean,
                                              Concavity_mean, Concave_points_mean, Symmetry_mean, Fractal_dimension_mean, Radius_se,
                                              Texture_se, Perimeter_se, Area_se, Smoothness_se, Compactness_se, Concavity_se, Concave_points_se,
                                              Symmetry_se, Fractal_dimension_se, Radius_worst, Texture_worst, Perimeter_worst, Area_worst,
                                              Smoothness_worst, Compactness_worst, Concavity_worst, Concave_points_worst, Symmetry_worst, Fractal_dimension_worst])

    st.success(diagnosis)


if __name__ == '__main__':
    main()
