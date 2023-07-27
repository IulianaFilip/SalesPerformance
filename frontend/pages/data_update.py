import streamlit as st
import pandas as pd

API_URL = "http://localhost:8501/sales_app"

st.markdown("# Add update")



quarters = st.selectbox("Please select quarter",["Q1", "Q2", "Q3"])
category = st.selectbox("Please select category",["Sales metric calcutation","individual performance tracking", "team performance tracking"])
subcategory = st.selectbox("Please select subcategory",["Revenue", "Unit sold", "Conversion rate","Sales targets", "Achived sales","Team targets", "Overall revenue"])
change_made = st.text_input("What do you want to change?")
report_made = st.text_area("Reason", "Please explain your change.")
output = st.text_area("Recomandations", "What futher action you recomand.")

if st.button("Submit"):
    st.write("Update submitted successfully.")
    
    data = {
        
        "quarters": quarters,
        "category": category,
        "subcategory": subcategory,
        "change_made": change_made,
        "report_made": report_made,
        "output": output
        
    }