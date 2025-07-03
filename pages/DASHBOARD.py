import streamlit as st
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PIL import Image
import streamlit.components.v1 as components

## TO SHOW FULL LOGO WHEN SIDEBAR IS OPENED WITH SOME DESCRIPTION
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

# TITLE
st.title("DASHBOARD 📈")
st.divider()

# SHOW GOAL AND TIME
if "goal" in st.session_state and "time" in st.session_state:
    st.write(f"🎯 Goal Amount: ₹{st.session_state.goal:,.2f}")
    st.write(f"📅 Time to Achieve: {st.session_state.time} months")
    
    
else:
    st.warning("⚠️ No goal data found. Please set your goal on the first page.")

st.write(f"To save {st.session_state.goal} in {st.session_state.time} months:")

#TABLE TO INPUT INCOME AND NECESSARY EXPENSES
st.header("STEP 2: Enter your income and necessary expences that can't be reduced ✍️", divider="gray")

default_data = {
        "Amount(in rupees)": [10,10,10,10,10],
    
    }

row_names = ["Income", "Utilities", "Rent","Groceries","Other necessary expenses"]

# Create DataFrame with row index names
default_df = pd.DataFrame(default_data, index=row_names)

# Step 1: Initialize table in session_state (only once)
if "spending_table" not in st.session_state:
    st.session_state["spending_table"] = default_df.copy()

# Show editable table
edited_df = st.data_editor( st.session_state["spending_table"], num_rows="dynamic", use_container_width=True , key="table1")

# Step 3: Save user edits back to session state
if st.button("Save Data"):
    st.session_state["spending_table"] = edited_df.copy()
    st.success("Spending data saved")

# BUTTON TO CALCULATE SPENDING MONEY
if st.button("Calculate"):
    try:
        income = edited_df.loc["Income", "Amount(in rupees)"]
        utilities = edited_df.loc["Utilities", "Amount(in rupees)"]
        rent = edited_df.loc["Rent", "Amount(in rupees)"]
        groceries = edited_df.loc["Groceries", "Amount(in rupees)"]
        other = edited_df.loc["Other necessary expenses", "Amount(in rupees)"]

        expenses=utilities + rent + groceries + other
        savings = income - utilities - rent - groceries - other
        st.session_state["savings"] = savings
        col1, col2,  = st.columns(2)
        col1.metric("Income", f"{income}",f"{income}")
        col2.metric("Savings",f"{savings}" ,f"{-expenses}" )
        st.success(f"💰 Your max savings are of : ₹{savings:,.2f}")
        st.info(f"Please head to the Budget page 👈 OR Enter this months savings if it's the end of the month 📝")

    except KeyError as e:
        st.error(f"Missing data: {e}")
st.divider()


st.header("STEP 4: Monthly Log 📋", divider="gray")  

# Step 1: Create default monthly log table
start_date = datetime.today()
months = [(start_date + relativedelta(months=i)).strftime("%B %Y") for i in range(st.session_state.time)]
monthly_data = {
    "amount(in rupees)": [10] + [0]*(st.session_state.time-1)
}
monthly_df = pd.DataFrame(monthly_data, index=months)

# Step 2: Create default data (if not already in session_state)
if "monthly_log" not in st.session_state:
 
 st.session_state["monthly_log"] = monthly_df.copy()

# Step 3: Show editable table
edited_monthly_df = st.data_editor(
    st.session_state["monthly_log"],
    num_rows="dynamic",
    use_container_width=True,
    key="table2"
)

# Step 4: Save data only on button click
if st.button("Save Monthly Log"):
 st.session_state["monthly_log"] = edited_monthly_df.copy()
 st.success("✅ Monthly log saved")

 #  Calculate and display total
 total = st.session_state["monthly_log"]["amount(in rupees)"].sum()
 st.subheader("🏁 Summary :" , divider="gray")
 st.success(f"🧾 Total Amount Saved: ₹{total:,.2f} / ₹{st.session_state.goal:,.2f} .")

 # SMALL POP UP IF GOAL ACHIEVED USING TOAST
 if int(total) >= int(st.session_state.goal):
    st.toast("🎉 Goal Achieved! Great job! 🎯", icon="✅")
    st.success("CONGRATS YOU DID IT 🏆")  
 else: 
   st.warning(f"You are {(total /st.session_state.goal)*100}% there!!")
   st.info("Do'nt give up ! 💪 Keep going 🌟")   