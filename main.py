import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.subheader("Data Dashboard")
uploaded_file = st.file_uploader("**Plz input a csv file**",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview : ")
    st.table(df.head())
    st.subheader("Data Summary")
    st.table(df.describe())
    st.subheader("Filter : ")
    column = df.columns.to_list()
    selected_column = st.selectbox("Select column to filter : ",column)
    unique_values = df[selected_column].unique()
    selected_value= st.selectbox("Select Value",unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.table(filtered_df)
    st.subheader("Visual Data")
    x_column = st.selectbox("Select X Axis : ",column)
    y_column = st.selectbox("Select Y Axis : ",column)

    button_css = """
<style>
    .gradient-button {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    .gradient-button:hover {
        background: linear-gradient(90deg, #feb47b, #ff7e5f);
    }
</style>
"""
    st.markdown(button_css, unsafe_allow_html=True)
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.warning("Can't find a file.")
