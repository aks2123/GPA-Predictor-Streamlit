
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
df = pd.read_csv ('Copy of SAT GPA - Sheet1.csv')
X = df.iloc [:,:-1].values
y = df.iloc [:,-1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestRegressor
reg_rf = RandomForestRegressor(n_estimators=18)
reg_rf.fit (X_train,y_train)
y_pred = reg_rf.predict (X_test)
import joblib
joblib.dump (reg_rf,'model.sav')
