import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image



# TO SHOW FULL LOGO WHEN SIDEBAR IS OPENED WITH SOME DESCRIPTION 
with st.sidebar:
 img = Image.open("sidebar1.jpg")
 resized_img = img.resize((500, 50))  
 st.sidebar.image(resized_img)
 st.sidebar.markdown("*Welcome to Budget Buddy! 🎉*")
 st.sidebar.markdown("*I hope this site makes budgeting easier 😊*")

# ONLY SHOW SMALL LOGO AT TOP LEFT CORNER
img = Image.open("logo1.png").convert("RGBA") 
resized_img = img.resize((60, 60)) 
st.image(resized_img)

#TITLE OF THE PG
st.title("HOME FINANCE MANAGEMENT APP")
st.divider()
st.header("STEP 1: Enter your details")
st.divider()

# Preserve name using session state
if "name" not in st.session_state:
    st.session_state.name = ""

# Text input to update session state
name = st.text_input("Enter your name", value=st.session_state.name, key="name_input")

# Update session state only if name changes
if name != st.session_state.name:
    st.session_state.name = name
# Display name
if st.session_state.name:
    st.write(f"Hello, {st.session_state.name} 😊")
st.divider()

# Preserve income using session state
if "income" not in st.session_state:
    st.session_state.income = 120.00

# Text input to update session state    
income=st.number_input("Enter your monthly income :",min_value=1.0, value=st.session_state.income, step=10.0 , key="income_input")

# Update session state only if income changes
if income != st.session_state.income:
    st.session_state.income = income

st.divider()

# Preserve goal amt to be saved using session state
if "goal" not in st.session_state:
    st.session_state.goal = 120.00

# number input to update session state
goal=st.number_input("Enter your goal amt to be saved :",min_value=1.0, value=st.session_state.goal, step=10.0 , key="goal_input")

# Update session state only if goal amt changes
if goal != st.session_state.goal:
    st.session_state.goal = goal

st.divider()

# Preserve time to achieve goal using session state
if "time" not in st.session_state:
    st.session_state.time = 12

# number input to update session state
time=st.slider("In how many months do you wish to achieve this goal ?",0,100, value=st.session_state.time , key="time_input" )

# Update session state only if time to achieve goal changes
if time != st.session_state.time:
    st.session_state.time = time

#TO SHOW USER HOW MUCH THEY NEED TO SAVE IN A MONTH 
if income and goal and time:
    if income > int(goal)/time:
        st.info(f"To save ₹{goal} in {time} months you need to ssve atleast ₹{int(goal)/time} per month")
        st.warning(f"YOU ARE SAVING APPROXIMATELY {int(((int(goal)/time)*100)/income)}% OF YOUR MONTHLY INCOME")
        
    else:
        st.error(f"Sorry your goal isnt achievable 😢 .Please enter a longer timeframe ❗")

# Initializing amt to be saved every month
max=int(goal)/time
st.session_state["max"] =max

# BUTTON TO SAVE GOAL AMT & TIME 
if st.button("Save Goal"):
    st.session_state.goal = goal
    st.session_state.time = time
    st.success("✅ Goal and timeline saved successfully!")
    st.info("Please go to dashboard 👈")



    