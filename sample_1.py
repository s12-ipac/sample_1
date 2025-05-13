# -*- coding: utf-8 -*-
"""
Created on Tue May 13 14:51:23 2025

@author: ipac survey
"""

import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

st.title("📱 Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    result = None
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    
    st.success(f"✅ Result: {result}")
