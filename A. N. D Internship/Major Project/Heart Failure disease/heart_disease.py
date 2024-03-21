import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Disease ",
                   layout="wide",
                   page_icon="🧑‍⚕️")

heart_Disease_model=pickle.load(open('E:/Python Projects/A. N. D Internship/Major Project/Heart Failure disease/heart_disease_model.sav','rb'))


st.title('Heart Disease Prediction')


col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex(Enter 1 For male and 0 For Female)')

with col3:
    cp = st.text_input('Chest Pain types(0-4)')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholestoral in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1:True & 0:False) ')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results (0-2)')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flourosopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
heart_diagnosis = ''

    # creating a button for Prediction

if st.button('Heart Disease Test Result'):

    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    user_input = [float(x) for x in user_input]

    heart_prediction = heart_Disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)
