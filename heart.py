import streamlit as st
import joblib
st.title('HEART DISEASE PREDICTION')
model= joblib.load('Heart_Disease_Prediction.joblib')
A= st.number_input('Enter age')
S= st.number_input('Enter gender (M:1,FM:0)')
C= st.number_input('Enter in digits')
B= st.number_input('Enter blood pressure')
P= st.number_input('Enter cholesterol')
F = st.number_input('Enter FBS(Y:1,N:0)')
E= st.number_input('Enter results')
M= st.number_input('Enter max hr')
X = st.number_input('Enter exercise agina(Y:1,N:0)')
T= st.number_input('Enter st depression')
L= st.number_input('Enter slope of st')
N= st.number_input('Enter no of vesselsfluro')
X= st.number_input('Enter thallium percentage')
if st.button('Predict Heart Disease'):
    prediction=model.predict([[A,S,C,B,P,F,E,M,X,T,L,N,X]])
    if prediction=='Y':
        st.text('Heart disease presence')
    else:
        st.text('Heart disease absence')
