import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")

ham_df = read_csv('hamilton_stats.csv')