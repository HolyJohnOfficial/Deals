# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:37:29 2025

@author: HJNmusicBaby
"""

import streamlit as st
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


pd.options.future.infer_string = True

#PHASE 1

st.title("Sales Performance Through Probabilistic Analysis")
st.write("Select a name to get started.")

#List of names: Sales Reps
names = ["Select a name", "Amir", "Karl", "Splendor", "Shalom", "Tosin", "Holy John", "Tessa", "Sekinat"]

#Dropdown
selected_name = st.selectbox("Choose a name", names)

#Only run the rest of the code below if valid name is chosen
if selected_name!= "Select a name":
    st.write(f"You selected: {selected_name}")
    uploaded_file = st.file_uploader("Choose a file")

    
    #...................PHASE 2.................
    #DATA INGESTION AND CLEANING
  
        #Dictect file type by extension
    if uploaded_file is not None:
        try:
            file_name = uploaded_file.name.lower() #Get the name of the uploaded file
            if file_name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif file_name.endswith((".xlsx", ".xls")):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Please upload a CSV or Excel file.")
                st.stop()

            #Remove duplicate rows
            df.drop_duplicates(inplace=True)
        
            #Rename column if exists
            if "Unnamed: 0" in df.columns:
                df.rename(columns={"Unnamed: 0":"sales_pitch_id"})
            
            #Validation check
            req_columns = {"status", "client", "product", "amount"}
            missing_cols = req_columns - set(df.columns)
        
            if len(missing_cols) > 0:
                st.error(f"The uploaded file is missing required columns {missing_cols}")
                st.stop()
            
            df['amount'] = df['amount'].abs()
        
            st.success(f"{file_name} has been cleaned and validated.")
        except Exception as e:
            st.write(f"An error occured while cleaning the file {e}.")
            
        #--------------PHASE 3: CORE METRICS-----------------
        p_success = (df['status'] == "Won").mean().round(4) * 100
        p_failure = (df['status'] == "Lost").mean().round(4) * 100
    
        #Win-rate per client type
        new_client_win = (df.groupby("client").get_group("New")["status"] == "Won").mean().round(3) * 100
        current_client_win = (df.groupby("client").get_group("Current")["status"] == "Won").mean().round(3) * 100

        #Spread (standard deviation of the sales amount)
        amount_std = round(df['amount'].std(), 3)
        
        #Status storage
        status_bin = (df['status'] == "Won").astype(int).to_list()
        
        #Create a function to calculate the longest consecutive streak of a givien value
        def longest_streak(collection, value):
            max_run = 0 #longest streak found so far
            current = 0 #Length of the current ongoing streak
        
            #Looping through the collection
            for c in collection:
                if c == value: #If the current value 'c' is a match with our specified 'value'
                    current += 1
                    max_run = max(max_run, current)
                else:
                    current = 0
            return max_run
        longest_win_streak = longest_streak(status_bin, 1)
        longest_lost_streak = longest_streak(status_bin, 0)


        #Conditional Probability
        #Collect outcomes that follows a win and those that follows a lost
        after_win = []
        after_lost = []
        
        for index in range(len(status_bin)-1):
            if status_bin[index] == 1:
                after_win.append(status_bin[index+1])
            else:
                after_lost.append(status_bin[index+1])
        
        #Computing conditional probability
        p_win_after_win = np.mean(after_win).round(4) * 100
        p_win_after_lost = np.mean(after_lost).round(4) * 100
        
        #Product Win rate
        product_win_rate = df.groupby("product")["status"].apply(lambda s: (s == "Won").mean()).round(3) * 100
        top_5_product_winrate = product_win_rate.nlargest(5)
        

        st.write("")
        st.write("")
        
        #----------------PHASE 4: SUMMARY TABLE--------------------
        st.subheader(f"{selected_name}'s Performance:")
        data = {"Metrics":["Success Rate", "Failure Rate", "New Client Win Rate", "Current Client Win Rate", "Longest Win Streak",
                           "Longest Loss Streak", "Probability of a Win after a win", "Probability of win after a loss", "Spreed"],
                "Values":[p_success, p_failure, new_client_win, current_client_win, longest_win_streak, longest_lost_streak,
                          p_win_after_win, p_win_after_lost, amount_std]}
        
        data_df = pd.DataFrame(data)
        st.dataframe(data_df, use_container_width=True)
        
        st.write("")
        st.write("")
        
        
        #--------------------PHASE 5: VISUALIZATION---------------------------
        st.subheader("Performance Visuals")
        fig, ax = plt.subplots()
        ax.hist(df['amount'], color='firebrick', edgecolor="white")
        ax.set_title(f"Distribution of {selected_name}'s Sales Amount.", color="white")
        
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        st.pyplot(fig)
        
        st.write("")
        
        fig, ax = plt.subplots()
        bars = ax.bar(top_5_product_winrate.index, top_5_product_winrate.values, color='blue', edgecolor="white")
        ax.bar_label(bars, labels = top_5_product_winrate.values, color="white")
        ax.set_title("Top 5 Product's by Win Rate%.", color="white")
        ax.set_yticks([])
        
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        st.pyplot(fig)
        
else:
    st.warning("Please select a valid name to continue.")