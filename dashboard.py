import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Assuming you have a function to predict demand
def predict_demand(date):
    # This is a placeholder function.
    # Replace it with your actual model prediction logic.
    np.random.seed(0)
    days_in_month = pd.date_range(start=date, periods=30, freq='D')
    demand_forecast = np.random.randint(100, 200, size=30)
    return pd.DataFrame({'date': days_in_month, 'demand': demand_forecast})

# Streamlit app
st.title("Demand Forecast for Inventory Management")

# Input: Date
input_date = st.date_input("Select a date", datetime.now())

if input_date:
    st.write(f"Demand forecast for the month starting from {input_date}")

    # Predict demand
    forecast_df = predict_demand(input_date)

    # Display prediction data
    st.write(forecast_df)

    # Plot prediction data
    plt.figure(figsize=(10, 5))
    plt.plot(forecast_df['date'], forecast_df['demand'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.title('Demand Forecast for the Month')
    plt.grid(True)
    st.pyplot(plt)
