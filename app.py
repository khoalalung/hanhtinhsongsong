import streamlit as st



model = pickle.load(open(filename, "rb"))
st.title('Revenue Prediction')
x_new = st.number_input('Input Temperature')
if st. button('Predict'):
	st.write('Revenue Prediction', y_new)
