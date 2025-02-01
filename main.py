#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn

# Model for employee query
class EmployeeQuery(BaseModel):
    department: str
    min_salary: int

@app.get("/employees/")
def get_employees(query: EmployeeQuery):
    conn = get_db_connection()
    employees = conn.execute(
        'SELECT * FROM Employees WHERE department = ? AND salary >= ?',
        (query.department, query.min_salary)
    ).fetchall()
    conn.close()

    return [dict(employee) for employee in employees]

