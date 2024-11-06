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
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.warning("Can't find a file.")
