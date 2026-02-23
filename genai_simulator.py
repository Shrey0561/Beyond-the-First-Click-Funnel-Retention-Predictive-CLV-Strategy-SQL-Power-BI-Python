import streamlit as st
import pandas as pd

st.title("GenAI Insights Simulator - Top CLV Customers")

df = pd.read_csv("top_customers.csv")  

st.subheader("Top CLV Customers")
st.dataframe(df)
st.subheader("Predicted CLV Distribution")
st.bar_chart(df['Predicted_CLV'])  

if st.button("Generate Insights"):
    st.write("Insights for Top CLV Customers:")
    for idx, row in df.iterrows():
        st.write(
            f"- Customer {row['Customer_Id']}: Likely to respond to personalized email campaigns, "
            f"upsell potential in {row['Preferred_Category']}, "
            f"loyalty score: {row['Loyalty_Score']}, churn risk: {row['Churn_Risk']}."
        )