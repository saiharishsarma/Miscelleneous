# Importing Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime as dt
from datetime import timedelta

st.set_page_config(layout= "wide")
st.title("A. Customer Data Simulation Tool")



# Creating Interface to enter required No of rows of the dataset 
nums = st.number_input('**Enter No of Rows needed in the data simulation(Ex: 500, 1000, etc.) :point_down::point_down:**')



# Considering different categories of product
categories = ['Electronics', 'Clothing', 'Food', 'Entertainment', 'Home and Garden', 'Beauty and Health']



# Using Loop for creation of sample data simuation
data=[]
for i in range(int(nums)):
    CustomerID= i+1
    VisitDate= (dt.date(2023,1,1)+ timedelta(days= random.randint(1,365))).strftime('%Y-%m-%d')
    TotalSpend = round(random.uniform(100,1000),0)
    ProductCategory = random.choice(categories)
    data.append([CustomerID, VisitDate, TotalSpend, ProductCategory])



# Creating Dataframe of the created sample dataset
df= pd.DataFrame(data,  columns= ['CustomerID','VisitDate', 'TotalSpend', 'ProductCategory'])


# Displaying Dataset on Streamlit Interface
if nums <=0:
    st.warning('Please enter a valid input')
else:
    st.success(":wave: Great! Dataset is generated. :wave:")
    st.dataframe(df)


    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)


    st.download_button(
        label="Download dataset as CSV",
        data=csv,
        file_name='samplename.csv',
        mime='csv')


# Streamlit Dashboarding

st.title("B. Customer Behaviour Analysis and Suggestion Tool")

# Creating Interface to upload CSV dataset file to get analysis and suggestions.
uploaded_file = st.file_uploader("**Upload your CSV file here**", type = ['csv'])
if uploaded_file:
    data= pd.read_csv(uploaded_file)

    # Basic EDA
    
    st.subheader("Basic Exploratory Data Analysis of the Dataset:", divider= "rainbow")
    st.write(f"Size of the Dataset: {data.shape}")
    st.write("*First 5 rows of the dataset:*")
    st.write(data.head())
    st.write("*Lst 5 rows of the dataset:*")
    st.write(data.tail())
    st.write("*Statistical Summary of the dataset:*")
    st.write(data.describe())
    st.write("*No of Unique entries in each column:*")
    st.write(data.nunique())
    st.write("*Check for missing values:*")
    st.write(data.isnull().sum())



  
    # Extracting KPIs
    if data.shape[1] ==4:

        AVG_Spent_Per_Customer = round(data['TotalSpend'].mean(), 2)
        MIN_Spent_Per_Customer = round(data['TotalSpend'].min(), 2)

        Popular_Product_Category = data['ProductCategory'].mode()[0]

        Monthly_AVG_Revenue_Growth= round(data.groupby(data['VisitDate'].str[0:7])['TotalSpend'].sum().mean(),2)
        Monthly_MIN_Revenue_Growth= round(data.groupby(data['VisitDate'].str[0:7])['TotalSpend'].sum().min(),2)
    else:
        st.warning("This dataset is not useful in this analysis. Kindly upload the correct file!")


    # Creating Suggestions to be appeared.

    Suggestions = []
    if AVG_Spent_Per_Customer < MIN_Spent_Per_Customer:
        Suggestions.append("Target Low-Spending Customers by personalized recommendations to increase their spend")

    if Popular_Product_Category:
        Suggestions.append(f"Launch More promotions for {Popular_Product_Category} category to boost the sales")

    if Monthly_AVG_Revenue_Growth < Monthly_MIN_Revenue_Growth:
        Suggestions.append("Attract More Customers by offering Discounts")


    # Adding KPIs Information to the Streamlit dashboard
    st.subheader("**Key Performance Indicators (KPIs):**", divider='rainbow')

    st.metric("**1. Average Money Spent Per Customer(in USD):**", AVG_Spent_Per_Customer)

    st.metric("**2. Most Popular Product Category:** ", Popular_Product_Category)

    st.metric("**3. Monthly Revenue Growth(in USD):** ", Monthly_AVG_Revenue_Growth)


    # Adding Suggestions to the Streamlit Dashboard
    st.subheader("Suggestions: ", divider= "rainbow")
    for i in Suggestions:
        st.markdown(f"***{i}**")
    
    st.success(":wave: Thanks for using! Have a nice day. :wave:")



    
    

    

    
