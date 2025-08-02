import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RetailCortex – Operational Simulation", layout="wide")
st.title("RetailCortex – Operational Scenario Simulator")

uploaded_file = st.file_uploader("Upload your master dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_simulated = df.copy()

    st.sidebar.header("Scenario Configuration")

    # Transport Budget Simulation
    transport_delta = st.sidebar.slider("Adjust Transport Cost (%)", min_value=-50, max_value=100, value=0, step=5)
    if transport_delta != 0:
        df_simulated["transport_cost_per_unit"] *= (1 + transport_delta / 100)

    # Promo Budget Simulation
    promo_delta = st.sidebar.slider("Adjust Promotional Effectiveness (%)", min_value=-100, max_value=100, value=0, step=5)
    if promo_delta != 0:
        df_simulated["promo_effectiveness"] *= (1 + promo_delta / 100)

    # Staff Cost per Unit
    staff_delta = st.sidebar.slider("Adjust Staff Cost per Unit (%)", min_value=-50, max_value=100, value=0, step=5)
    if staff_delta != 0:
        df_simulated["staff_cost_per_unit"] *= (1 + staff_delta / 100)

    # Close Store
    store_ids = sorted(df["store_id"].unique())
    store_to_close = st.sidebar.multiselect("Temporarily Close Store(s)", store_ids)
    if store_to_close:
        df_simulated = df_simulated[~df_simulated["store_id"].isin(store_to_close)]

    # Focus on a specific product
    product_focus = st.sidebar.selectbox("Focus on Product (optional)", ["All"] + sorted(df["product_id"].unique().tolist()))
    if product_focus != "All":
        df_simulated = df_simulated[df_simulated["product_id"] == product_focus]

    st.subheader("Key Performance Indicators (KPI)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transport Cost", f"{df_simulated['transport_cost_per_unit'].sum():,.2f}")
    col2.metric("Avg. Promo Effectiveness", f"{df_simulated['promo_effectiveness'].mean():.2f}")
    col3.metric("Total Staff Cost", f"{df_simulated['staff_cost_per_unit'].sum():,.2f}")

    st.subheader("Export Simulated Data")
    st.download_button(
        label="Download Simulated CSV",
        data=df_simulated.to_csv(index=False),
        file_name="retailcortex_simulation.csv",
        mime="text/csv"
    )

    st.subheader("Simulated Table Preview")
    st.dataframe(df_simulated.head(30), use_container_width=True)
else:
    st.info("Please upload your dataset to begin.")
