import streamlit as st
from src.read import Reader
from src.validator import Validator

st.title("Personal Finance Analyser")
st.markdown("""
## Welcome!

Upload your **transaction CSV** to begin.

### Our app will:

- Validate your data
- Analyze income and expenses
- Display charts
- Generate financial insights
""")
st.markdown("---")

#---Uploading block---
st.sidebar.header("Upload")
file = None
file = st.sidebar.file_uploader("Upload your csv file",type=["csv"])
if file != None:
    st.sidebar.write(f"Successfully uploaded the {file.name}")


#---Validation Block---
st.header("Validation")

st.markdown("---")

#---Finance Summary---
st.header("Finance Summary")
col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("Income")
with col2:
    st.subheader("Expense")
with col3:
    st.subheader("Savings")

st.markdown("---")

#---Charts Block---
st.header("Charts")

st.markdown("---")

#---Finance Block---
st.header("Finance Insights")

