import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sample Duration Calculator", layout="centered")
st.title("📊 Sample Size & Duration for MoE (1% to 5%)")

# Integer input fields
agents = st.number_input("Enter number of agents", min_value=1, value=10, step=1, format="%d")
cfperagent = st.number_input("Enter calls per agent per day", min_value=1, value=100, step=1, format="%d")
ac = st.number_input("Enter number of ACs", min_value=1, value=100, step=1, format="%d")
dist = st.number_input("Enter number of districts", min_value=1, value=30, step=1, format="%d")

# When "Calculate" is pressed
if st.button("Calculate"):
    results = []

    for MoE in range(1, 6):  # 1 to 5
        MoE_prop = MoE / 100
        base_sample = ((1.96 * 0.5) / MoE_prop) ** 2

        sample_state = round(base_sample)
        duration_state = round(sample_state / agents / cfperagent, 2)

        sample_ac = round(base_sample * ac)
        duration_ac = round(sample_ac / agents / cfperagent, 2)

        sample_dist = round(base_sample * dist)
        duration_dist = round(sample_dist / agents / cfperagent, 2)

        results.append({
            "MoE (%)": MoE,
            "State Sample": sample_state,
            "State Duration (days)": duration_state,
            "AC Sample": sample_ac,
            "AC Duration (days)": duration_ac,
            "District Sample": sample_dist,
            "District Duration (days)": duration_dist
        })

    df = pd.DataFrame(results)
    st.subheader("📋 Results Table")
    st.dataframe(df.style.format({
        "State Sample": "{:,}",
        "AC Sample": "{:,}",
        "District Sample": "{:,}",
        "State Duration (days)": "{:.2f}",
        "AC Duration (days)": "{:.2f}",
        "District Duration (days)": "{:.2f}"
    }))
