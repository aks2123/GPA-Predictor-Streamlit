import streamlit as st
from prediction import predict
import numpy as np

st.title ('GPA predictor from SAT Score')
st.write ('Please select SAT score and press the ***Predict GPA*** button')


sat = st.number_input ('select', min_value= 400, max_value= 1600)

if st.button ('Predict GPA'):
    GPA = predict ([[sat]])
    st.write ('GPA would be', GPA)
    