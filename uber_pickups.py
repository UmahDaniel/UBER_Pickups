# Building my uber pick up app

# First step is to import the libraries

import streamlit as st
import pandas as pd
import numpy as np


# Create a title
st.title("Uber Pickups in NYC") 
st.write("This app is to analyze Uber pickups in NYC by Daniel Umah the Product Gee")




# Run streamlit from the commannd line
# streamlit run uber_pickups.py

# Fetching Data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'  'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN    
    ] = pd.to_datetime(data[DATE_COLUMN])
    return data

    # Create a text element and let the reader know the data is loading.

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data')
st.write(data)

# Draw a histogram

#To start, let's add a subheader just below the raw data section:

st.subheader('Number of pickups by hour')

# Use NumPy to generate a histogram that breaks down pickup times binned by hour:

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# Now, let's use Streamlit's st.bar_chart() method to draw this histogram.

st.bar_chart(hist_values)   

# Plot data on a map
st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

#Filter results with a slider
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

#Use a button to toggle data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

    