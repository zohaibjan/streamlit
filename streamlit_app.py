import streamlit as st

# import pandas to read the our data file
import pandas as pd

st.title("🤖 Machine Learning App")

st.write("Welcome to world of Machine Learning with Streamlit.")

# read the csv file
df = pd.read_csv("data/penguins_cleaned.csv")
df
