import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import load_model
import yfinance as yf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_local('Stockpic.jpg')


def generate_forecasts(company_name, forecast_date):
    # download the data
    df = yf.download(tickers=[f'{company_name}.NS'], period='1y')
    y = df['Close'].fillna(method='ffill')
    y = y.values.reshape(-1, 1)

    # scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(y)
    y = scaler.transform(y)

    # generate the input and output sequences
    n_lookback = 60  # length of input sequences (lookback period)
    n_forecast = 30  # length of output sequences (forecast period)

    X = []
    Y = []

    for i in range(n_lookback, len(y) - n_forecast + 1):
        X.append(y[i - n_lookback: i])
        Y.append(y[i: i + n_forecast])

    X = np.array(X)
    Y = np.array(Y)

    # fit the model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(n_lookback, 1)))
    model.add(LSTM(units=50))
    model.add(Dense(n_forecast))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, Y, epochs=100, batch_size=32, verbose=0)

    # generate the forecasts
    X_ = y[-n_lookback:]  # last available input sequence
    X_ = X_.reshape(1, n_lookback, 1)

    Y_ = model.predict(X_).reshape(-1, 1)
    Y_ = scaler.inverse_transform(Y_)

    # organize the results in a data frame
    df_past = df[['Close']].reset_index()
    df_past.rename(columns={'index': 'Date', 'Close': 'Actual'}, inplace=True)
    df_past['Date'] = pd.to_datetime(df_past['Date'])
    df_past['Forecast'] = np.nan
    df_past.loc[df_past.index[-1], 'Forecast'] = df_past.loc[df_past.index[-1], 'Actual']

    df_future = pd.DataFrame(columns=['Date', 'Actual', 'Forecast'])
    df_future['Date'] = pd.date_range(start=df_past['Date'].iloc[-1] + pd.DateOffset(days=1), periods=n_forecast)
    df_future['Actual'] = np.nan
    df_future['Forecast'] = Y_.flatten()

    results = df_past.append(df_future).set_index('Date')

    return results


st.markdown("<h1 style='color: yellow;'>Stock Price Forecasting</h1>", unsafe_allow_html=True)

# User inputs
st.markdown("<h3 style='color: yellow;'>Company Name</h3>", unsafe_allow_html=True)
company_name = st.text_input('', 'RELIANCE')


st.markdown("<h3 style='color: yellow;'>Forecast Start Date</h3>", unsafe_allow_html=True)
forecast_date = st.date_input('', value=pd.to_datetime('today'))


if st.button('Generate Forecast'):
    with st.spinner('Generating forecasts...'):
        results = generate_forecasts(company_name, forecast_date)
        st.markdown("<h2 style='color: yellow;'>Forecasted Stock Prices</h2>", unsafe_allow_html=True)
        st.line_chart(results[['Actual', 'Forecast']])

