import streamlit as st
from src.read import Reader

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
st.sidebar.header("Upload")
file = None
file = st.sidebar.file_uploader("Upload your csv file",type=["csv"])
if file != None:
    st.sidebar.write(f"Successfully uploaded the {file.name}")
