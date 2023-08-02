import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://localhost:8501/sales_app"

st.markdown("# Data collection")
if 'data' not in st.session_state:
    st.session_state.data = {}  
else:
    st.write("Previous report:")
    st.write(st.session_state.data)
    
  
name  = st.text_input("Enter your name")


quarter = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3"])
metric_calculation = st.selectbox("Select sales metric calculation", ["Revenue", "Unit sold", "Conversion rate"])
individual_performance = st.selectbox("Select individual performance tracking", ["Sales targets", "Achived sales", "Conversion rate"])
team_performance = st.selectbox("Select team performance tracking", ["Team targets", "Overall revenue", "Conversion rate"])
customer_behavior = st.selectbox("Select customer behavior analysis", ["Patterns", "Trends", "segment customer"])


if st.button("Submit"):
    st.write("Report submitted successfully.")
    
    data = {
        "name": name,
        "quarter": quarter,
        "metric_calculation": metric_calculation,
        "individual_performance": individual_performance,
        "team_performance": team_performance,
        "customer_behavior": customer_behavior,
        
        
    }

    st.session_state.data = data


