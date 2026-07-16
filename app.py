import streamlit as st
import pandas as pd
from src.read import Reader
from src.validator import Validator
from src.analyser import Analyser
from src.visualizer import Visualizer
from src.insights import InsightGenerator
st.title("📊Personal Finance Analyser")
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

#-----Uploading block-----
st.sidebar.header("📂Upload")
file = None
file = st.sidebar.file_uploader("Upload your csv file",type=["csv"])
if file != None:
    st.sidebar.write(f"Successfully uploaded the {file.name}")

validation_result = False
if file != None:
    #---Validation Block---
    st.header("Validation Status")
    read = Reader(file)
    df = read.read_csv()
    validator = Validator(df)
    validation_result = validator.validate()

    if(validation_result != True):
        st.error(validation_result)
    else:
        st.success("CSV validated successfully. Ready for analysis.")
        st.markdown("---")


        #---Analysis Block---
        analysis = Analyser(df)
        analysed_results = analysis.analyse()

        #---Finance Summary---
        st.header("Finance Summary")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.metric("💰Total Income",analysed_results["total_income"])
        with col2:
           st.metric("💸Expense",analysed_results["total_expense"])
        with col3:
            st.metric("🏦Savings",analysed_results["total_savings"])

        st.markdown("---")

        #---Charts Block---
        st.header("Charts")

        visualize = Visualizer(analysed_results)
        income_fig = visualize.income_bar(analysed_results["category_income"])
        expense_fig = visualize.expense_bar(analysed_results["category_expense"])
        savings_fig = visualize.expense_income_savings_bar(analysed_results["total_expense"],analysed_results["total_income"],analysed_results["total_savings"])
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Income")
            st.pyplot(income_fig)
        with col2:
            st.subheader("Expense")
            st.pyplot(expense_fig)
        st.subheader("Savings")
        st.pyplot(savings_fig)


        st.markdown("---")

        #---Finance Block---
        st.header("Finance Insights")
        generate = InsightGenerator(analysed_results)
        insights = generate.generate()
        for insight in insights:
            st.write("-",insight)


