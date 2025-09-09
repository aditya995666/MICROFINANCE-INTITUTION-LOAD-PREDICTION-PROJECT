import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Microfinance Loan Prediction", layout="wide")


@st.cache_resource
def load_model():
    with open("best_model_rf.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

import os
st.image("microfinance_image.png" ,use_container_width=True)

st.title(" Microfinance Loan Prediction")
st.write("Predict the probability of loan repayment within 5 days.")

features = [
    "daily_decr30", "daily_decr90", "rental30", "rental90", "last_rech_amt_ma", "cnt_ma_rech30", 
    "sumamnt_ma_rech30", "cnt_ma_rech90", "sumamnt_ma_rech90", "cnt_loans30", "amnt_loans30", 
    "maxamnt_loans30", "cnt_loans90", "payback90"
]

st.header(" Upload a CSV file for predictions")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    try:
        data = data[features]

        data = data.apply(pd.to_numeric, errors='coerce')

        data = data.fillna(0)

        st.write(" Preview of Cleaned Data:")
        st.dataframe(data.head())

        if st.button(" Predict from CSV"):
            predictions = model.predict(data)
            st.success("Prediction Completed!")

            data["Prediction"] = ["Non-Defaulter" if p == 1 else " Defaulter" for p in predictions]
            st.dataframe(data.head())

            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button(" Download Predictions", csv, "loan_predictions.csv", "text/csv")

    except KeyError as e:
        st.error(f"Error: Missing required columns - {e}")

st.sidebar.header("Enter Details Manually")
st.sidebar.write("Fill in the features below to get a prediction.")

input_data = {}
for feature in features:
    input_data[feature] = st.sidebar.number_input(f"{feature}", value=0.0, format="%.2f")

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

if st.sidebar.button("Predict Manually"):
    prediction = model.predict(input_df)
    st.sidebar.write(" Prediction:", "Non-Defaulter" if prediction[0] == 1 else " Defaulter")

