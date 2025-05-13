import streamlit as st
import pandas as pd

st.set_page_config(page_title="Duration Calculator", layout="centered")
st.title("📞 Calling Plan Calculator")

# Input fields
agents = st.number_input("Enter number of agents", min_value=1, value=100, step=1, format="%d")
cfperagent = st.number_input("Enter avg cf per agent per day", min_value=1, value=12, step=1, format="%d")
ac = st.number_input("Enter number of ACs", min_value=1, value=100, step=1, format="%d")
dist = st.number_input("Enter number of districts", min_value=1, value=30, step=1, format="%d")

# Button to trigger calculation
if st.button("Calculate"):
    results = []

       for MoE in range(1, 6):  # MoE from 1% to 5%
            MoE_prop = MoE / 100
            base_sample = ((1.96 * 0.5) / MoE_prop) ** 2

            sample_state = round(base_sample)
            duration_state = math.ceil(sample_state / agents / cfperagent)

            sample_ac = round(base_sample * ac)
            duration_ac = math.ceil(sample_ac / agents / cfperagent)

            sample_dist = round(base_sample * dist)
            duration_dist = math.ceil(sample_dist / agents / cfperagent)

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

    st.subheader("📋 Result")

    # Custom styling functions
    def highlight_moe(val):
        return "background-color: #ffe599"  # Light yellow for MoE column

    def header_style():
        return [
            {'selector': 'thead th', 'props': [('background-color', '#d9ead3'), ('color', 'black')]}
        ]

    styled_df = (
        df.style
        .format({
            "Sample - State Level": "{:,}",
            "Duration - State Level": "{:,}",
            "Sample - AC Level": "{:,}",
            "Duration - AC Level": "{:,}",
            "Sample - District Level": "{:,}",
            "Duration - District Level": "{:,}"
        })
        .applymap(highlight_moe, subset=["MoE"])
        .set_table_styles(header_style())
    )

    st.dataframe(styled_df, use_container_width=True)
