import streamlit as st
import pandas as pd

st.header("Bar Chart with Complex Equation")

# Generate sample data using a complex equation
x = range(1, 11)
y = [2 * (n ** 2) + 3 * n + 5 for n in x]

data = {"x": x, "y": y}
df = pd.DataFrame(data)

# Display the DataFrame
st.write(df)

# Create a bar chart using the generated data
st.bar_chart(data=df, x="x", y="y")
