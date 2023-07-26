import streamlit as st
import pandas as pd

API_URL = "http://localhost:8501/sales_app"

st.markdown("# Add update")
st.text_input("What do you want to update?")


quarter = st.text_input("Enter your quarter")
metric_calculation = st.selectbox("Select sales metric calcutation", ["Revenue", "Unit sold", "Conversion rate"])
individual_performance = st.selectbox("Select individual performance tracking", ["Sales targets", "Achived sales", "Conversion rate"])
team_performance = st.selectbox("Select team performance tracking", ["Team targets", "Overall revenue", "Conversion rate"])
change_made = st.text_input("What do you want to change?")


if st.button("Submit"):
    st.write("Update submitted successfully.")
    
    data = {
        
        "quarter": quarter,
        "metric_calculation": metric_calculation,
        "individual_performance": individual_performance,
        "team_performance": team_performance,
        
        
        
    }