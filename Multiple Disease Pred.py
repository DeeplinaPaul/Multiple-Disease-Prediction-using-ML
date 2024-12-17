# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:50:26 2024

@author: Deeplina Paul
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System using ML', 
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'], 
                           
                           icons = ['activity', 'heart'],
                           
                           default_index = 0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    

    
    Pregnancies = st.text_input('Number of Pregnancies', key = 'pregnancy')
    Glucose = st.text_input('Glucose Level', key = 'glucose')
    BloodPressure = st.text_input('Blood Pressure Value', key = 'bloodpressure')
    SkinThickness = st.text_input('Skin Thickness Value', key = 'skinthickness')
    Insulin = st.text_input('Insulin Level', key = 'insulin')
    BMI = st.text_input('BMI Level', key = 'bmi')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', key = 'pedigreefunction')
    Age = st.text_input('Age of the Person', key = 'age')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
        
        else:
            diab_diagnosis = 'The Person is not Diabetic'
        
    st.success(diab_diagnosis)    
    
    
# Heart Disease Prediction Page
# Diabetes Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    

    
    Age = st.number_input('Age of the Person', key = 'age')
    Sex = st.number_input('Sex of the Person', key = 'sex')
    CP = st.number_input('Chest Pain Type', key = 'cp')
    Trestbps = st.number_input('Resting Blood Pressure', key = 'trestbp')
    Chol = st.number_input('Serum Cholestoral', key = 'sc')
    FBS = st.number_input('Fasting Blood Sugar', key = 'fbs')
    Restecg = st.number_input('Resting Electrocardiographic Results', key = 'restecg')
    Thalach = st.number_input('Maximum Heart Rate Achieved', key = 'thalach')
    Exang = st.number_input('Exercise Induced Angina', key = 'ex')
    OldPeak = st.number_input('ST depression induced by exercise relative to rest', key = 'old') 
    Slope = st.number_input('The Slope of the peak exercise ST segment', key = 'slope')
    CA = st.number_input('Number of major vessels (0-3) colored by Flourosopy', key = 'ca')
    Thal = st.number_input('Thallium Heart Rate', key = 'thal')
    
    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[Age, Sex, CP, Trestbps, Chol, FBS, Restecg, Thalach, Exang, OldPeak, Slope, CA, Thal]])
    
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The Person has Heart Disease'
        
        else:
            heart_diagnosis = 'The Person does not have a Heart Disease'
        
    st.success(heart_diagnosis)
    