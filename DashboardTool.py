# Streamlit Dashboarding
import streamlit as st
import pandas as pd
st.title("Customer Behaviour Analysis and Suggestion Tool")

# Creating Interface to upload CSV dataset file to get analysis and suggestions.
uploaded_file = st.file_uploader("**Upload your CSV file here**", type = ['csv'])
if uploaded_file:
    data= pd.read_csv(uploaded_file)

    # Extracting KPIs

    Avg_Spent_Per_Customer = round(data['Money_Spent'].mean(), 2)

    Popular_Product_Category = data['Product_Category'].mode()[0]

    Monthly_Revenue_Growth= round(data.groupby(data['Date_Visited'].str[0:7])['Money_Spent'].sum().mean(),2)


    # Creating Suggestions to be appeared based on hypothetically designed threshold values

    Suggestions = []
    if Avg_Spent_Per_Customer < 300:
        Suggestions.append("Target Low-Spending Customers by personalized recommendations to increase their spend")

    if Popular_Product_Category:
        Suggestions.append(f"Launch More promotions for {Popular_Product_Category} category to boost the sales")

    if Monthly_Revenue_Growth < 40000:
        Suggestions.append("Attract More Customers by offering Discounts")


    # Adding KPIs Information to the Streamlit dashboard
    st.subheader("**Key Performance Indicators (KPIs)**", divider='rainbow')

    st.metric("**1. Average Money Spent Per Customer(Threshold: 300):**", Avg_Spent_Per_Customer)

    st.metric("**2. Most Popular Product Category:** ", Popular_Product_Category)

    st.metric("**3. Monthly Revenue Growth(Threshold: 40,000):** ", Monthly_Revenue_Growth)


    # Adding Suggestions to the Streamlit Dashboard
    for i in Suggestions:
        st.markdown(f"***{i}**")
