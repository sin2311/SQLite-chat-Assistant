#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests

st.title("Employee Query System")

department = st.text_input("Enter Department:")
min_salary = st.number_input("Enter Minimum Salary:", min_value=0)

if st.button("Search"):
    if department and min_salary:
        response = requests.get(
            "http://127.0.0.1:8000/employees/",
            params={"department": department, "min_salary": min_salary}
        )

        if response.status_code == 200:
            employees = response.json()
            if employees:
                for emp in employees:
                    st.write(f"Name: {emp['name']}, Salary: {emp['salary']}")
            else:
                st.write("No employees found.")
        else:
            st.write("Error querying the API.")
    else:
        st.write("Please fill out all fields.")


# In[1]:


import streamlit as st


# In[2]:


# Save the code as a Python file
with open("streamlit_app.py", "w") as f:
    f.write("""import streamlit as st
import requests

st.title("Employee Query System")

department = st.text_input("Enter Department:")
min_salary = st.number_input("Enter Minimum Salary:", min_value=0)

if st.button("Search"):
    if department and min_salary:
        response = requests.get(
            "http://127.0.0.1:8000/employees/",
            params={"department": department, "min_salary": min_salary}
        )

        if response.status_code == 200:
            employees = response.json()
            if employees:
                for emp in employees:
                    st.write(f"Name: {emp['name']}, Salary: {emp['salary']}")
            else:
                st.write("No employees found.")
        else:
            st.write("Error querying the API.")
    else:
        st.write("Please fill out all fields.")""")

