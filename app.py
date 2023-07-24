import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load the dataset from a CSV file
data = pd.read_csv("Streamlit_data.csv")

# Loading the saved machine learning model
model = pickle.load(open('CCP.pkl', 'rb'))

# Function for making predictions using the loaded model
def prediction(input_data):
    model_pred = model.predict([input_data])

    if model_pred == [0]:
        return 'Client Not subscribed to the Insurance'
    else:
        return 'Client subscribed to the Insurance'

# Main function to run the Streamlit app
def main():
    # Setting the title of the Streamlit app
    st.title('Customer Conversion Prediction')
    #main image
    pic = Image.open('health-insurance.jpg')
    st.image(pic,  width=750)
    # Sidebar image for the app
    image = Image.open('Insurance.jpg')
    st.sidebar.image(image, width=220)

    # Adding a sidebar option for prediction
    selected_option = st.sidebar.selectbox("Select Option", ["Prediction", "About"])

    if selected_option == "Prediction":
        # Getting user inputs using various input widgets
        age1 = st.text_input("Enter Person Age")

        # Dropdown menu for selecting the occupation
        job1 = st.selectbox('Select the occupation', ['blue-collar', 'entrepreneur', 'housemaid', 'services', 'technician',
                                                      'self-employed', 'admin.', 'management', 'unemployed', 'retired',
                                                      'student'])

        # Dropdown menu for selecting the marital status
        marital1 = st.selectbox('Select Marital status', ["divorced", "married", "single"])

        # Dropdown menu for selecting the Education Qualification
        education1 = st.selectbox('Select Education qualification', ["primary", "secondary",  "tertiary"])

        # Dropdown menu for selecting the Call Type
        call_type1 = st.selectbox('Select last contact communication type', ["unknown", "telephone", "cellular"])

        # Dropdown menu for selecting the Month
        month1 = st.selectbox('Select the month',
                              ['may', 'jul', 'jan', 'nov', 'jun', 'aug', 'feb', 'apr', 'oct', 'sep', 'dec', 'mar'])

        day1 = 0
        # Select the date based on the selected month
        if month1 in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
            day1 = st.selectbox('Select the date',
                                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                 26, 27, 28, 29, 30, 31])
        elif month1 in ['apr', 'jun', 'sep', 'nov']:
            day1 = st.selectbox('Select the date',
                                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                 26, 27, 28, 29, 30])
        elif month1 == 'feb':
            day1 = st.selectbox('Select the date',
                                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                 26, 27, 28])

        # Text input for duration
        dur1 = st.text_input('Last contact duration (in seconds)')

        # Text input for number of calls
        num_calls1 = st.text_input('Enter the Number of Calls')

        # Dropdown menu for previous outcome
        prev_outcome1 = st.selectbox('Select outcome of the previous marketing campaign',
                                     ["unknown", "failure", "other", "success"])

        # Dictionary for encoding data for model input
        job = {'blue-collar': 0, 'entrepreneur': 1, 'housemaid': 2, 'services': 3, 'technician': 4,
               'self-employed': 5, 'admin.': 6, 'management': 7, 'unemployed': 8, 'retired': 9, 'student': 10}
        marital = {"divorced": 0, "married": 1, "single": 2}
        education = {"primary": 0, "secondary": 1, "tertiary": 2}
        call_type = {"unknown": 0, "telephone": 1, "cellular": 2}
        month = {'may': 0, 'jul': 1, 'jan': 2, 'nov': 3, 'jun': 4, 'aug': 5, 'feb': 6, 'apr': 7, 'oct': 8, 'sep': 9,
                 'dec': 10, 'mar': 11}
        prev_outcome = {"unknown": 0, "failure": 1, "other": 2, "success": 3}

        # Code for making predictions and displaying results
        results = ''

        if st.button('Predict'):
            # Perform the necessary encoding and data processing for prediction
            results = prediction(
                [int(age1), job[job1], marital[marital1], education[education1], call_type[call_type1], int(day1),
                 month[month1], int(dur1), int(num_calls1), prev_outcome[prev_outcome1]])
        st.success(results)
    elif selected_option == "About":
        st.title('Welcome to Insurance Prediction')
        st.write("""
**Health Insurance**:

Health insurance covers the cost of an insured individual's medical and surgical expenses. 
Subject to the terms of insurance coverage, either the insured pays costs out-of-pocket and is subsequently reimbursed, 
or the insurance company reimburses costs directly.
""")
        st.write("""
**A Health Insurance policy is:**

A contract between an insurance provider and an individual or his/her sponsor. The contract can be renewable (annually, monthly) or lifelong in the case of private insurance. It can also be mandatory for all citizens in the case of national plans. The type and amount of health care costs that will be covered by the health insurance provider are specified in writing, in a member contract or "Evidence of Coverage" booklet for private insurance, or in a national [health policy] for public insurance.
""")

        st.write("""
**About Streamlit:**

Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers. Data scientists or machine learning engineers are not web developers and they're not interested in spending weeks learning to use these frameworks to build web apps. Instead, they want a tool that is easier to learn and to use, as long as it can display data and collect needed parameters for modeling. Streamlit allows you to create a stunning-looking application with only a few lines of code.
""")


if __name__ == '__main__':
    main()
