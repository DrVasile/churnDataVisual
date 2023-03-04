import streamlit

from utils.plot_util import show_plots

streamlit.header("Marketing Dashboard")

features = ["MULTIPLAY", "PRET_ABON"]

show_plots(features)
