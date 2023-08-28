import streamlit as st
import joblib
import numpy as np

def predict (data):
    lr = joblib.load ('model.sav')
    return lr.predict (data)
