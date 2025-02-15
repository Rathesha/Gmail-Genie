import streamlit as st

# Get query parameters
query_params = st.query_params

# Check if 'code' exists in the URL
if "code" in query_params:
    auth_code = query_params["code"]
    st.success(f"Authorization successful! Code: {auth_code}")
else:
    st.error("No authorization code found. Please try again.")
