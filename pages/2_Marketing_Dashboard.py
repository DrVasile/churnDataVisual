import streamlit

from utils.plot_util import load_data, show_plots

streamlit.header("Marketing Dashboard")

data_frame = load_data()

features = ["PERIOADA", "CONTRACT_LENGTH", "CONTRACT_START_DATE", "CONTRACT_EXPIRATION_DATE"]

show_plots(data_frame, features)
