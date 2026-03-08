import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_pipeline.nse_data import get_nifty_price, get_option_chain
from engines.options_engine import calculate_pcr

st.title("Beast Trading AI")

price = get_nifty_price()

option_data = get_option_chain()

pcr = calculate_pcr(option_data)

if price is not None:
    st.metric("NIFTY Price", price)
else:
    st.write("NIFTY price unavailable")

if pcr is not None:
    st.write("Put Call Ratio:", pcr)
else:
    st.write("PCR unavailable (NSE API blocked or unavailable)")
