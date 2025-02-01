#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests

# URL for your FastAPI back-end
API_URL = "http://your-fastapi-url.com"  # Replace with your actual FastAPI URL

# Streamlit app title
st.title("Employee Query System")

# Query type selection
query_type = st.selectbox(
    "Select your query type:",
    [
        "Show all employees in the department",
        "Who is the manager of the department?",
        "List all employees hired after a date",
        "Total salary expense for the department"
    ]
)

# Department input (for most queries)
department = st.text_input("Enter Department:")

# Additional inputs based on query type
if query_type == "List all employees hired after a date":
    hire_date = st.text_input("Enter Hire Date (YYYY-MM-DD):")
else:
    hire_date = None

if query_type == "Total salary expense for the department":
    min_salary = None
else:
    min_salary = None

# Button to submit query
if st.button('Submit'):
    if query_type == "Show all employees in the department":
        response = requests.get(f"{API_URL}/employees/by_department", params={"department": department})
    elif query_type == "Who is the manager of the department?":
        response = requests.get(f"{API_URL}/department/manager", params={"department": department})
    elif query_type == "List all employees hired after a date":
        response = requests.get(f"{API_URL}/employees/hired_after", params={"hire_date": hire_date})
    elif query_type == "Total salary expense for the department":
        response = requests.get(f"{API_URL}/department/total_salary", params={"department": department})

    # Handle response
    if response.status_code == 200:
        data = response.json()
        if "message" in data:
            st.write(data["message"])  # Display error messages
        else:
            st.write(data)  # Display result
    else:
        st.write("Error with the query. Please try again.")

