import streamlit as st
import pandas as pd

st.header("Salary and Experience Bar Graph")

# Sample data for salary and experience
data = {"Experience": [1, 3, 5, 2, 4],
        "Salary": [50000, 60000, 70000, 55000, 65000]}

df = pd.DataFrame(data)

# Display the DataFrame
st.write(df)

# Create a bar chart using the salary and experience data
st.bar_chart(data=df, x="Experience", y="Salary", color="blue", height=400)
