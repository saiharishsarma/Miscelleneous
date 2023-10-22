
# Importing Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime as dt
from datetime import timedelta

st.set_page_config(layout= "wide")
st.title("Sample Customer Spending Data Simulation Tool")



# Creating Interface to enter required No of rows of the dataset 
nums = st.number_input('**Enter No of Rows needed in the data simulation**')



# Considering different categories of product
categories = ['Electronics', 'Clothing', 'Food', 'Entertainment', 'Home_and_Garden', 'Beauty_and_Health']



# Using Loop for creation of sample data simuation
data=[]
for i in range(int(nums)):
    Customer_ID= i+1
    Date_Visited= (dt.date(2023,1,1)+ timedelta(days= random.randint(1,365))).strftime('%Y-%m-%d')
    Money_Spent = round(random.uniform(30,1000),0)
    Product_Category = random.choice(categories)
    data.append([Customer_ID, Date_Visited, Money_Spent, Product_Category])



# Creating Dataframe of the created sample dataset
df= pd.DataFrame(data,  columns= ['Customer_ID','Date_Visited', 'Money_Spent', 'Product_Category'])


# Displaying Dataset on Streamlit Interface
st.dataframe(df)
 
# Saving the dataset to a CSV file in the system  
title= st.text_input(f"**Enter a Name to Save CSV file( For Ex: filename.csv)**")
if title:
    df.to_csv(title, index= True)
    st.success(f" CSV '*{title}*' Saved Sucessfully!!, Kindly Check the file Under Users Folder")






# Streamlit Dashboarding

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

