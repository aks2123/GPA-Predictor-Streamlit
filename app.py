import streamlit as st
from prediction import predict
import numpy as np

st.title ('GPA predictor from SAT')
st.write ('Hello World!')
r = st.radio ('Select GPA', (1000, 5000, 1000))
if r == 1000:
    st.write ('Nice one')
else:
    st.write ('try again')

st.slider ('select', min_value= 10, max_value= 100)

sat = st.number_input ('select', min_value= 400, max_value= 1600)

if st.button ('Predict GPA'):
    GPA = predict ([[sat]])
    st.write ('GPA IS', GPA)
    