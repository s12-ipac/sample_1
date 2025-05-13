# -*- coding: utf-8 -*-
"""
Created on Tue May 13 14:51:23 2025
@author: ipac survey
"""

import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("📱 Sample Size & Duration Calculator")

# Input fields
MoE = st.number_input("Enter Margin of Error (%)", value=5.0)
agents = st.number_input("Enter number of agents")
cfperagent = st.number_input("Enter cf per agent")
ac = st.number_input("Enter number of ACs")
dist = st.number_input("Enter number of districts")

# Calculation
if st.button("Calculate"):
    try:
        MoE_prop = MoE / 100
        base_sample = ((1.96 * 0.5) / MoE_prop) ** 2

        sample_state = round(base_sample)
        duration_state = round(sample_state / agents / cfperagent, 2)

        sample_ac = round(base_sample * ac)
        duration_ac = round(sample_ac / agents / cfperagent, 2)

        sample_dist = round(base_sample * dist)
        duration_dist = round(sample_dist / agents / cfperagent, 2)

        st.subheader("📈 Results")
        st.markdown(f"**Total Sample (State):** {sample_state}")
        st.markdown(f"**Estimated Duration (State Level):** {duration_state} days")
        st.markdown(f"**Total Sample (All ACs):** {sample_ac}")
        st.markdown(f"**Estimated Duration (AC Level Total):** {duration_ac} days")
        st.markdown(f"**Total Sample (All Districts):** {sample_dist}")
        st.markdown(f"**Estimated Duration (District Level Total):** {duration_dist} days")

    except ZeroDivisionError:
        st.error("❌ Make sure Margin of Error, agents, and cf per agent are not zero.")
