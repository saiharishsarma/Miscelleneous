
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
    st.success(f" CSV '*{title}*' Saved Sucessfully!, Kindly Check the file Under Users Folder.")