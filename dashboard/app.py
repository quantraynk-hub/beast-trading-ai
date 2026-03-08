import streamlit as st

from data_pipeline.nse_data import get_nifty_price, get_option_chain
from engines.options_engine import calculate_pcr

st.title("Beast Trading AI")

price = get_nifty_price()

option_data = get_option_chain()

pcr = calculate_pcr(option_data)

st.metric("NIFTY Price", price)

st.write("Put Call Ratio:", pcr)
