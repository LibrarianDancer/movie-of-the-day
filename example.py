import streamlit as st
import pandas as pd

# Google Sheet의 URL
sheet_url = "https://docs.google.com/spreadsheets/d/1q0Qenp-9mDzEJ-x_Z2f9O7oEYVVlxefxLW7mM90vRnk/export?format=csv"

# 데이터 읽어들이기
df = pd.read_csv(sheet_url)

# Streamlit 앱 만들기
st.title("Google Sheet Data Analysis")
st.write(df)

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")