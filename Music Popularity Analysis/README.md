# 🧐 Music Popularity Prediction with Machine Learning

Music popularity prediction involves developing machine learning models to estimate the popularity of music tracks based on their audio features. Predicting the popularity of music can help music streaming platforms understand user preferences, optimize playlists, and enhance recommendation systems to improve user engagement and satisfaction.

This project demonstrates how to train a Machine Learning model for music popularity prediction using Python.

# 🔍 Overview

Music popularity prediction means using regression techniques to forecast the popularity of songs based on various music features and metadata. This project aims to provide accurate predictions of a song’s future performance in terms of streams, downloads, and chart positions. Such predictions enable music producers, artists, and marketers to make informed decisions.

# ⏳ Dataset ⏳

For this project, we use a dataset containing 227 music tracks, each described by their music features and additional metadata such as track name, artists, album name, and release date. The dataset is ideal for training and evaluating machine learning models for music popularity prediction.

# Features Influencing Popularity 🌟
Based on correlation analysis and visualizations, the following features show significant relationships with popularity and are used to train the prediction model:

- Energy  
- Valence  
- Danceability  
- Loudness  
- Acousticness  
- Tempo  
- Speechiness  
- Liveness  

These features capture various audio characteristics that influence how popular a music track becomes.

# Model Training 🤖 🧠
The project involves:

Exploratory data analysis to understand feature distributions and correlations with popularity.
Feature selection based on correlation analysis.
Training a regression model to predict music popularity using Python and relevant libraries such as scikit-learn and pandas.
Results and Evaluation
The model's predictions are evaluated against actual popularity values. Visualizations and metrics are used to assess prediction accuracy and identify areas for improvement.
