import streamlit as st
import numpy as np
import joblib

# Set the page configuration
st.set_page_config(page_title='Multiclass Classification', layout='wide')

# Cache the loading of the model
@st.cache_resource(show_spinner='Loading model...')
def load_model():
    return joblib.load("./models/multiclass_model.joblib")

@st.cache_resource(show_spinner='Loading ...')
def load_encoder():
    return joblib.load("./models/encoder.joblib")
 

def multiclass_prediction():
   
    st.title('Multiclass Prediction')

    # Load the trained multiclass model
    model = load_model()
    encoder = load_encoder()

    # Create input fields for the features
    st.header('Enter the input features:')
    T1 = st.number_input('T1')
    T2 = st.number_input('T2')
    T3 = st.number_input('T3')
    T4 = st.number_input('T4')
    T5 = st.number_input('T5')
    T6 = st.number_input('T6')
    T7 = st.number_input('T7')
    T8 = st.number_input('T8')
    T9 = st.number_input('T9')
    T10 = st.number_input('T10')
    T11 = st.number_input('T11')
    T12 = st.number_input('T12')
    T13 = st.number_input('T13')
    T14 = st.number_input('T14')
    T15 = st.number_input('T15')
    T16 = st.number_input('T16')
    T17 = st.number_input('T17')
    T18 = st.number_input('T18')

    # Button for making prediction
    if st.button('Predict'):

        # To prepare the input features
        input_data = np.array([[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18]])

        # To make the prediction
        prediction = model.predict(input_data)

        # Inverse transform the prediction to decode it
        decod_prediction = encoder.inverse_transform(prediction)

        # Display the prediction
        st.write(f'The predicted class is: {decod_prediction[0]}')

if __name__ == '__main__':
    multiclass_prediction()

