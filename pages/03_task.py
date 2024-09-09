import streamlit as st
import pandas as pd
from task import create_output  

def run_app():
    st.set_page_config(page_title='Activity Analysis', layout='wide')
    st.title('Activity Analysis')

    # File uploader for Excel files
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

    if uploaded_file is not None:
        
        df = pd.read_excel(uploaded_file)

        # Generate the output using the imported function
        output = create_output(df)

        # Display the output DataFrame
        st.header('Generated Output')
        st.dataframe(output)

       

if __name__ == '__main__':
    run_app()
