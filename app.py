import streamlit as st
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

model = pickle.load(open('model.pickle', "rb"))
y_new = model.predict(x_new)

st.title('Revenue Prediction')
x_new = st.number_input('Input Temperature')
if st. button('Predict'):
	st.write('Revenue Prediction', y_new)
