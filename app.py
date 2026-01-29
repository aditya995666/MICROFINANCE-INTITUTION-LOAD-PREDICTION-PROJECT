import streamlit as st
import pandas as pd
import joblib
from datetime import date

from utils.preprocess import preprocess_input
from utils.pdf_reader import read_pdf

pipeline = joblib.load("model/churn_pipeline.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

display_names = {
    "age_on_network_days": "Customer Age on Network (Days)",
    "avg_daily_decr_30d": "Avg Daily Decrement (30 Days)",
    "avg_daily_decr_90d": "Avg Daily Decrement (90 Days)",
    "total_rental_30d": "Total Rental (30 Days)",
    "total_rental_90d": "Total Rental (90 Days)",
    "count_ma_recharges_30d": "Recharge Count (30 Days)",
    "sum_amt_ma_recharges_30d": "Total Recharge Amount (30 Days)",
    "median_amt_ma_recharges_30d": "Median Recharge Amount (30 Days)",
    "median_ma_rech_prebal_30d": "Median Pre-Balance (30 Days)",
    "count_ma_recharges_90d": "Recharge Count (90 Days)",
    "sum_amt_ma_recharges_90d": "Total Recharge Amount (90 Days)",
    "median_amt_ma_recharges_90d": "Median Recharge Amount (90 Days)",
    "median_ma_rech_prebal_90d": "Median Pre-Balance (90 Days)",
    "days_since_last_recharge": "Last Recharge Date"
}

st.set_page_config(page_title="Churn Prediction App", layout="wide")
st.title("Customer Churn Prediction System")

tab1, tab2 = st.tabs(["Manual Input", "File Upload"])


with tab1:
    st.subheader("Enter Customer Details")

    user_data = {}
    cols = st.columns(3)

    for i, col in enumerate(feature_columns):

        if col == "days_since_last_recharge":
            last_recharge_date = cols[i % 3].date_input(
                "Last Recharge Date",
                value=date.today()
            )
            user_data[col] = (date.today() - last_recharge_date).days

        else:
            label = display_names.get(col, col)
            user_data[col] = cols[i % 3].number_input(label, value=0.0)

    if st.button("Predict Churn"):
        df = pd.DataFrame([user_data])
        df = preprocess_input(df, feature_columns)

        pred = pipeline.predict(df)[0]
        proba = pipeline.predict_proba(df)[0][1]

        st.success(f"Prediction: {'Loan Repay' if pred==1 else 'Not Loan Repay'}")
        st.info(f"Churn Probability: {proba:.2f}")


with tab2:
    st.subheader("Upload PDF / CSV / TXT File")

    uploaded_file = st.file_uploader(
        "Upload File",
        type=["pdf", "csv", "txt"]
    )

    if uploaded_file is not None:
        file_ext = uploaded_file.name.split(".")[-1].lower()

        if file_ext == "pdf":
            df = read_pdf(uploaded_file)
            if df is None:
                st.error(" No table found in PDF")

        elif file_ext == "csv":
            df = pd.read_csv(uploaded_file)

        elif file_ext == "txt":
            df = pd.read_csv(uploaded_file, delimiter=",")

        else:
            df = None

        if df is not None:
            st.success("File Loaded Successfully")
            st.dataframe(df.head())

            df_clean = preprocess_input(df, feature_columns)

            df["Churn_Prediction"] = pipeline.predict(df_clean)
            df["Churn_Probability"] = pipeline.predict_proba(df_clean)[:, 1]

            st.success("Prediction Completed")
            st.dataframe(df.head())

            st.download_button(
                "Download Result CSV",
                df.to_csv(index=False),
                file_name="churn_predictions.csv",
                mime="text/csv"
            )
