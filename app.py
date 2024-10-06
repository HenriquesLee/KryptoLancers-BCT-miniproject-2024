# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account, get_balance, send_transaction

# Web3 connection
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Set the background image using HTML and CSS
background_image = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://media1.tenor.com/m/HkBmWN8onyUAAAAC/bg.gif") no-repeat center center fixed;
    background-size: cover;
}

[data-testid="stSidebarContent"] {
    background-image: linear-gradient(to bottom right, #290e47, #341c5c);
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

################################################################################
# KryptoLancers Candidate Information
candidate_database = {
    "Lee": [
        "Lee", "0x8040a966458e991E9B2D118dB9d9B3C884ab7b3D", "5.0 ⭐", 1.5, "Images/Lee.jpg"
    ],
    "Shreya": [
        "Shreya", "0x46c99e3B379db258819dF8c6ED0f9Eb2184D205F", "1.0 ⭐", 0.33, "Images/Shreya.jpg"
    ],
    "Yash_G": [
        "Yash_G", "0x8087f66eDf2FF6F3578A492fC2bcf8d008507f51", "4.7 ⭐", 1.0, "Images/Ganar.jpg"
    ],
    "Yash_B": [
        "Yash_B", "0xF42f5A999e2AbF3173F7e35A4b5f5b51d03Eaa50", "4.1 ⭐", 0.85, "Images/bhalekar.png"
    ],
}

people = ["Lee", "Shreya", "Yash_G", "Yash_B"]

################################################################################
# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Step 1 - Generate Account from Private Key
private_key = "0xdd8335260c4c49a4d6ef4ead9f9802fbe2356e26a275b87f0feb20549e4c4acc"  # Replace with your actual private key

# Use Web3 to generate an account using the private key
account = w3.eth.account.from_key(private_key)

# Display the client's Ethereum account address in the sidebar
st.sidebar.write("Ethereum Address: ", account.address)

# Display the account balance in Ether
st.sidebar.write("Balance: ", get_balance(w3, account.address))

################################################################################

# Select a candidate to hire
person = st.sidebar.selectbox("Select a Person", people)
hours = st.sidebar.number_input("Number of Hours")

# Candidate details
candidate = candidate_database[person][0]
hourly_rate = candidate_database[person][3]
candidate_address = candidate_database[person][1]

# Display candidate details in sidebar
st.sidebar.write("Candidate: ", candidate)
st.sidebar.write("Hourly Rate (ETH): ", hourly_rate)
st.sidebar.write("Candidate Address: ", candidate_address)

# Step 2: Calculate Wage and Send Transaction

# Calculate the wage
wage = hourly_rate * hours
st.sidebar.markdown("## Total Wage in Ether")
st.sidebar.write(wage)

# Button to send the transaction
if st.sidebar.button("Send Transaction"):
    # Call send_transaction function to send Ether from client to the candidate
    transaction_hash = send_transaction(w3, account, candidate_address, wage)
    
    # Display transaction hash in the sidebar
    st.sidebar.markdown("### Transaction Hash")
    st.sidebar.write(transaction_hash)

################################################################################
# Function to display candidates in the main app
def get_people():
    """Display the database of KryptoLancers candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoLancers Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

# Main headings
st.markdown("# KryptoLancers!")
st.markdown("## Hire A Engineering Freelancer Professional!")
st.text(" \n")

# Call function to display candidates
get_people()
