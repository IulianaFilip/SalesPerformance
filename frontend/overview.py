from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np  

API_URL = "http://localhost:8501/sales_app"




st.sidebar.markdown("# SalesPerformance")


st.title("Welcome to Sales Performance!")
st.write("Gain valuable insights into your sales data, track key metrics, and make data-driven decisions for sales success. Visualize trends with interactive charts, forecast future sales, and optimize performance. Set goals, analyze funnels, and segment customers. Export reports and collaborate seamlessly. Empower your sales team with actionable intelligence and achieve growth with ease.")


labels = "Customer behavior analysis", "Team Performance Tracking", "Individual Performance Tracking", "Sales metric Calculation"
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

st.pyplot(fig1)



data = pd.DataFrame({ 
    "Sales metric Calculation": ["Revenue", "Unit sold", "Conversion rate"],
    "Individual Performance Tracking": ["Sales targets", "Achived sales", "Conversion rate"],
    "Team Performance Tracking": ["Team targets", "Overall revenue", "Conversion rate"],
    "Customer behavior analysis": ["Patterns", "Trends", "segment customer"]
})
st.markdown("## Data")
col1, col2 = st.columns(2)

# Area Chart
col1.subheader("**")
col1.area_chart(data)


col2.subheader("**")
col2.line_chart(data)


col1.subheader("**")
col1.bar_chart(data)