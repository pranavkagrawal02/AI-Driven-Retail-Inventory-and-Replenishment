import pandas as pd
import streamlit as st
import numpy as np

st.title("🧠 AI-Driven Retail Inventory & Replenishment System")

file = st.file_uploader("Upload sales data (CSV)", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    st.subheader("Basic Summary")
    st.write(df.describe())
else:
    st.info("Please upload your dataset to begin.")
