# Apple Stock Price Analysis using Hybrid Model 

The provided dataset contains historical stock data for Apple Inc. from the past year. It features daily records with essential attributes such as Date, Open, High, Low, Close, and Volume. For this task, your primary focus should be on the Close price, which indicates the stock’s final trading price at the end of each day. The time-series nature of the dataset makes it ideal for sequential modeling, and its numerical structure is well-suited for regression analysis.

# 🔍 Problem Statement / Objective :

The primary objective is to develop a predictive model capable of accurately forecasting Apple Inc.’s stock prices for the next 10 days. Due to the complexity of stock market data, which can display both short-term sequential dependencies and broader trends, relying on a single model type may be insufficient. The challenge is to effectively capture these intricate patterns. Therefore, a hybrid modeling approach is required, combining LSTM (to capture time dependencies and short-term trends) and Linear Regression (to capture long-term trends).

Traditional models like Linear Regression (LR) excel at capturing linear trends, while Long Short-Term Memory (LSTM) networks are great for detecting complex, sequential patterns. By combining both, we achieve better accuracy and a more robust forecasting approach!
 

🔹 The hybrid model improved prediction stability compared to LSTM alone.
🔹 Feature selection for the LR model (adding more lag variables) significantly impacted accuracy.
🔹 Tuning the weights (70% LSTM, 30% LR) is crucial for balancing model performance.

# LSTM & LR :

We will be utilizing LSTM (Long Short-Term Memory) and Linear Regression models for this task. LSTM is chosen because it effectively captures sequential dependencies and patterns in time-series data, making it suitable for modeling stock price movements influenced by historical trends.

Linear Regression, on the other hand, is a straightforward model that captures simple linear relationships and long-term trends in data. By combining these two models into a hybrid approach, we leverage the LSTM’s ability to model complex time-dependent patterns alongside the Linear Regression’s ability to identify and follow broader trends. This combination aims to create a more balanced and accurate prediction system

# 📌 Project Breakdown:

✅ Data Preprocessing: Collected Apple stock price data, converted dates into a time-series format, and applied MinMax scaling.
✅ Feature Engineering: Created lag features to capture historical trends for the LR model.
✅ LSTM Model: Built a deep learning model with multiple LSTM layers to learn sequential patterns in stock prices.
✅ Linear Regression Model: Trained on lagged stock prices to complement the LSTM’s predictions.
✅ Hybrid Predictions: Combined predictions using a weighted average approach (70% LSTM, 30% LR).
✅ Future Forecasting: Predicted stock prices for the next 10 days using both models and the hybrid approach.

📊 Results:
The hybrid model provided more stable and accurate predictions compared to using LSTM or Linear Regression alone. Handled short-term fluctuations while capturing long-term dependencies effectively.
