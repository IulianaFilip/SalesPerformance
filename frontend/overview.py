import pandas as pd
import streamlit as st


API_URL = "http://localhost:8501/sales_app"



st.sidebar.markdown("# SalesPerformance")


st.title("Welcome to Sales Performance!")
st.write("Gain valuable insights into your sales data, track key metrics, and make data-driven decisions for sales success. Visualize trends with interactive charts, forecast future sales, and optimize performance. Set goals, analyze funnels, and segment customers. Export reports and collaborate seamlessly. Empower your sales team with actionable intelligence and achieve growth with ease.")



col1, col2, col3 = st.columns(3)

col1.metric(label="Sales",value="€ 1.000.000", delta="200%")
col2.metric(label="Time",value="3", delta="100%")
col3.metric(label="Value",value="150%", delta="+50%")    

#image_path = st.image(r"C:\Users\iulia\Desktop\OneDrive\Pictures\photo2.jpg")

data = pd.DataFrame({ 
    "Sales metric Calculation": ["Revenue", "Unit sold", "Conversion rate"],
    "Individual Performance Tracking": ["Sales targets", "Achived sales", "Conversion rate"],
    "Team Performance Tracking": ["Team targets", "Overall revenue", "Conversion rate"],
    "Customer behavior analysis": ["Patterns", "Trends", "segment customer"]
})

st.subheader("Line Chart:")
st.line_chart(data)
st.bar_chart(data)
st.markdown("## Data")
st.table(data)

