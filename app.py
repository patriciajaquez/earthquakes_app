#----------------------------------Libraries----------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
#------------------------------------------------------------------------------


#---------------------------------Page Config----------------------------------
set.set_page_config(
    page_title="Earthquake Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
#------------------------------------------------------------------------------


#----------------------------Title and Description-----------------------------
st.title("Earthquake Analysis Dashboard")
st.markdown("""
    This dashboard provides an analysis of earthquake data using various visualizations and clustering techniques.
    The data is sourced from the USGS Earthquake Catalog and includes information on earthquake magnitude, depth, and location.
    The dashboard allows users to explore the data through interactive charts and maps, as well as perform clustering analysis.
""")
#------------------------------------------------------------------------------


#-------------------------------Variables in None------------------------------
# The objective of this section is to define variables that will be used in the app.
# These variables are set to None initially and will be updated later in the app.
# This is done to avoid errors when the variables are referenced before they are defined.
filtered_df = None
df= None
#-------------------------------------------------------------------------------


#-------------------------------Load Data---------------------------------------
# The objective of this section is to cache the data loading process.
# This is done to improve performance and avoid reloading the data every time the app is run.
@st.cache_data(ttl=3600)
def load_data():
    try:
        df = pd.read_csv("data/all_month.csv")
        # Convert time column to datetime and arase the time zone
        df['time'] = pd.to_datetime(df['time'], unit='ms').dt.tz_localize(None)
        df['updated'] = pd.to_datetime(df['updated'], unit='ms').dt.tz_localize(None)
        # Additonal columns
        df['day'] = df['time'].dt.day
        df['hour'] = df['time'].dt.hour
        df['day_of_week'] = df['time'].dt.day_name()
        df['week'] = df['time'].dt.isocalendar().week
        df['month'] = df['time'].dt.month
        df['year'] = df['time'].dt.year
        df['date'] = df['time'].dt.date
        # Magnitude categories
        conditions = [
            (df['mag'] < 2.0),
            (df['mag'] >= 2.0) & (df['mag'] < 4.0),
            (df['mag'] >= 4.0) & (df['mag'] < 6.0),
            (df['mag'] >= 6.0)
        ]
        choices = ['Micro', 'Light', 'Moderate', 'Strong']
        df['magnitude_category'] = np.select(conditions, choices, default='Unknown')
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

