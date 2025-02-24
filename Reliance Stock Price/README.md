# 📈 Reliance Stock Price Prediction

## 📌 Overview
This project focuses on **predicting Reliance stock prices** using **Machine Learning and Deep Learning models**. The goal is to analyze historical stock data, identify trends, and forecast future prices for informed decision-making.

## 🚀 Features
- **Data Collection:** Retrieves historical stock data from Yahoo Finance/NSE API
- **Feature Engineering:** Includes Moving Averages, RSI, MACD, and Bollinger Bands
- **Sentiment Analysis:** Integrates news and social media sentiment for better accuracy
- **Machine Learning Models:** ARIMA, XGBoost, Random Forest
- **Deep Learning Models:** LSTM, GRU for time series forecasting
- **Evaluation Metrics:** RMSE, MAPE, R² Score
- **Interactive Dashboard:** Visualizes stock trends and predictions

## 📂 Dataset
- **Source:** Yahoo Finance, NSE/BSE APIs
- **Timeframe:** Historical data (daily, weekly, monthly)
- **Features:** Open, High, Low, Close, Volume, Technical Indicators, Sentiment Scores

## 🛠️ Technologies Used
- **Python** 🐍
- **Libraries:** Pandas, NumPy, Scikit-Learn, TensorFlow, Statsmodels
- **Time Series Analysis:** ARIMA, SARIMA, LSTM
- **Visualization:** Matplotlib, Seaborn, Plotly
- **API Integration:** Yahoo Finance, Alpha Vantage

## 📊 Model Performance
| Model               | RMSE  | MAPE  | R² Score  |
|--------------------|-------|-------|----------|
| ARIMA             | 3.45  | 2.8%  | 0.89     |
| Random Forest     | 2.98  | 2.3%  | 0.92     |
| LSTM              | 2.65  | 2.0%  | 0.95     |

## 🔧 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shivamjaiswal65435/reliance-stock-prediction.git
   cd reliance-stock-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the training script:
   ```bash
   python train.py
   ```
4. Predict stock prices:
   ```bash
   python predict.py --date "YYYY-MM-DD"
   ```

## 📌 Usage
- Analyze historical stock trends
- Predict future stock prices for investment strategies
- Visualize stock movements using an interactive dashboard

## 🔗 Connect with Me
👨‍💻 **Shivam Jaiswal**  
🔗 [GitHub](https://github.com/shivamjaiswal65435)  
🔗 [LinkedIn](https://www.linkedin.com/in/shivam-jaiswal65425/)  

📢 Feel free to fork, contribute, or raise issues! 🚀
