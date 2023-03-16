import streamlit as st
import pickle
from sklearn

model = pickle.load(open('model.pickle', "rb"))

st.title('Revenue Prediction')
x_new = st.number_input('Input Temperature')
y_new = model.predict(x_new)

if st. button('Predict'):
	st.write('Revenue Prediction', y_new)
