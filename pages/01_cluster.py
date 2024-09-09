import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title='Clustering', page_icon='', layout='wide')

def cluster_prediction():
    st.title('Cluster Prediction')
    cluster_model = joblib.load("./models/kmeans_pipeline.joblib")

    with st.form('user_input'):
        st.write('Enter the data to make the cluster prediction')

        # Create the input fields
        date = st.date_input('Date')
        time = st.time_input('Time')
        sensor = st.number_input('Sensor Value', min_value=0.00, step=0.1)
        location = st.text_input('Location')
        number = st.number_input('Number', min_value=1, step=1)
        activity = st.selectbox('Activity', ['placed', 'picked'])
        position = st.selectbox('Position', ['inside', 'outside'])
        

        submitted = st.form_submit_button('Get Prediction')

    # If the user submits the form
    if submitted:
        user_data = pd.DataFrame({
            'date': [date],
            'time': [time],
            'sensor': [sensor],
            'location': [location],
            'number': [number],
            'activity': [activity],
            'position': [position]
            

        })

        # Make prediction
        prediction = cluster_model.predict(user_data)

        # Display the prediction
        st.write(f"The predicted cluster for the given user data is: {prediction[0]}")

if __name__ == '__main__':
    cluster_prediction()