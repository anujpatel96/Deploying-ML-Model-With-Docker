import numpy as np
import pickle
import pandas as pd
# from flasgger import Swagger
import streamlit as st

from PIL import Image

# app=Flask(__name__)
# Swagger(app)

pickle_in = open("Detecting_Counterfeit_Money.pkl", "rb")
classifier = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_note_authentication(variance, skewness, curtosis, entropy):
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Counterfeit Money Detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <img src="https://i0.wp.com/morinvillenews.com/wp-content/uploads/2019/01/Counterfeit-Bills_1.jpg?fit=1600%2C900&ssl=1 width="180" height="383 " >
    <h2 style="color:white;text-align:center;">Streamlit Counterfeit Money Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result = ""
    if st.button("Predict"):
        result = int(predict_note_authentication(variance, skewness, curtosis, entropy))
        if result == 0:
            st.success('The Money is not counterfeit. The bill is Real =)')
        else:
            st.success('The Money is counterfeit. The bill is Fake =(')

    #st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
