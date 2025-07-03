import streamlit as st
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
resized_img = img.resize((60, 60))  # Adjust size as needed
st.image(resized_img)

# TITLE
st.title("LET'S BUDGET YOUR SPENDING! 💸" )
st.divider()
st.header("STEP 3: Adjust your other expenses " , divider="gray")

if "savings" in st.session_state:
 st.write(f"Your budget: ₹{st.session_state['savings']}") 
 
else:
    st.warning("Savings not calculated yet. Please go to Home page first.")

# DROPDOWN OPTIONS FOR SPENDING MODES
#step 1: Selection
option = st.multiselect(
    "How do you spend your money ❓",
    ["Transport", "Food", "Outing" , "Snacks" , "Clothing","Other"],
    
)
st.write("You selected:", option)

# Step 2: For each selected category, show a slider
spending = {}
total = 0
for category in option:
    amount = st.slider(
        f"How much do you spend on {category} ?",
        min_value=0,
        max_value=st.session_state['savings'],
        step=100,
        key=category  # use category as unique key for each slider
    )
    spending[category] = amount
    total += amount  # Add to total spending


# Step 3: Show result
if st.button("CALCULATE"):
    if spending:
     st.subheader("Your spending breakdown:")
     st.write(spending)
     st.info(f"💰 Total Spending: ₹{total}")

    if "savings" in st.session_state and "max" in st.session_state:
     if total > st.session_state['savings']:
         st.error("Oops your spendings are more than your savings 😢 .Please adjust your spendings ❗")#Shows error if ypuu spend more than you save
     elif  (st.session_state['savings']-total) >= st.session_state['max'] :
         st.write("Good job you are on the right track!") #is shown only when you save more than or equal to the required amt per month(calculated in the home pg)
     
         st.success(f" You saved: ₹{st.session_state['savings']-total} ")
         st.info(f" Go back to dashboard to enter your savings in your monthly log 👈 ")
         st.balloons() 
         
     else:
         st.error(f"Oops you're only saving: ₹{st.session_state['savings']-total} 😢 .Please adjust your spendings to save atleast ₹{st.session_state['max']}❗")

# FEEDBACK FROM USER (FACES)
selected = st.feedback(options="faces")
if selected is not None:
 st.markdown(f"You selected {selected} . Thankyou for the feedback! 😊")

you_saved=st.session_state['savings']-total
  

       
