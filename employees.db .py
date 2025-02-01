#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# Connect to SQLite (this will create the database file if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    FOREIGN KEY (department) REFERENCES Departments (name)
)
''')

# Insert some sample data
cursor.executemany('''
INSERT INTO Departments (name) VALUES (?)
''', [('HR',), ('Engineering',), ('Sales',)])

cursor.executemany('''
INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)
''', [
    ('Alice', 'Engineering', 60000),
    ('Bob', 'Sales', 50000),
    ('Charlie', 'HR', 40000),
    ('David', 'Engineering', 70000)
])

# Commit changes and close the connection
conn.commit()
conn.close()


# In[3]:


shutil.move('employees.db', 'employees.db')  # If the file is already in the current directory

