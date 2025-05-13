import streamlit as st
import pandas as pd

st.set_page_config(page_title="Duration Calculator", layout="centered")
st.title("Calling Plan Calculator")

# Input fields
agents = st.number_input("Enter number of agents", min_value=1, value=10, step=1, format="%d",value=100)
cfperagent = st.number_input("Enter avg cf per agent per day", min_value=1, value=100, step=1, format="%d", value=12)
ac = st.number_input("Enter number of ACs", min_value=1, value=100, step=1, format="%d")
dist = st.number_input("Enter number of districts", min_value=1, value=30, step=1, format="%d")

# Button to trigger calculation
if st.button("Calculate"):
    results = []

    for MoE in range(1, 6):  # MoE from 1% to 5%
        MoE_prop = MoE / 100
        base_sample = ((1.96 * 0.5) / MoE_prop) ** 2

        sample_state = round(base_sample)
        duration_state = round(sample_state / agents / cfperagent)

        sample_ac = round(base_sample * ac)
        duration_ac = round(sample_ac / agents / cfperagent)

        sample_dist = round(base_sample * dist)
        duration_dist = round(sample_dist / agents / cfperagent)

        results.append({
            "MoE": f"{MoE}%",
            "Sample - State Level": sample_state,
            "Duration - State Level": duration_state,
            "Sample - AC Level": sample_ac,
            "Duration - AC Level": duration_ac,
            "Sample - District Level": sample_dist,
            "Duration - District Level": duration_dist
        })

    df = pd.DataFrame(results)

    st.subheader("Calling Plan")

    # Beautify the table with commas and styling
    st.dataframe(
        df.style
        .format({
            "Sample - State Level": "{:,}",
            "Duration - State Level": "{:,}",
            "Sample - AC Level": "{:,}",
            "Duration - AC Level": "{:,}",
            "Sample - District Level": "{:,}",
            "Duration - District Level": "{:,}"
        })
        .applymap(
            lambda x: "background-color: lightgreen"
            if isinstance(x, (int, float)) and x > 100
            else "",
            subset=[
                "Duration - State Level",
                "Duration - AC Level",
                "Duration - District Level"
            ]
        )
    )
