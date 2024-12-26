import streamlit as st
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import MDS
from scipy.spatial.distance import pdist, squareform
from statsmodels.graphics.tsaplots import plot_acf
from io import BytesIO

st.title("Nifty 50 Stock Analysis Dashboard (2023)")

# Define parameters for data download
start_date = '2023-01-01'
end_date = '2023-12-31'
nifty_symbols = {
    'Reliance': 'RELIANCE.NS', 'TCS': 'TCS.NS', 'Infosys': 'INFY.NS', 
    # Add sector mapping to symbols
    'HDFC Bank': 'HDFCBANK.NS', 'ICICI Bank': 'ICICIBANK.NS',
}

sectors = {
    'Energy': ['Reliance'],
    'Technology': ['TCS', 'Infosys'],
    'Banking': ['HDFC Bank', 'ICICI Bank'],
}

# Download adjusted closing prices for all Nifty 50 stocks
@st.cache_data
def load_data(symbols, start, end):
    data = yf.download(list(symbols.values()), start=start, end=end)['Adj Close']
    data = data.dropna()  # Drop rows with any missing values
    return data

data = load_data(nifty_symbols, start_date, end_date)
st.success("Data loaded successfully!")

# Sidebar: Select sector and stocks
selected_sector = st.sidebar.selectbox("Select Sector", options=['All'] + list(sectors.keys()))
if selected_sector != 'All':
    selected_stocks = sectors[selected_sector]
else:
    selected_stocks = list(nifty_symbols.keys())

selected_stocks = st.sidebar.multiselect(
    "Select Stocks for Analysis",
    options=selected_stocks,
    default=selected_stocks
)

# Map selected stock names to their symbols
selected_stock_symbols = [nifty_symbols[stock] for stock in selected_stocks]
data = data[selected_stock_symbols]

st.write("### Stock Price Data")
st.write(data.head())

# Time Series Plot
st.subheader("Time Series Plot")
st.line_chart(data)

# Log Returns Calculation
log_returns = np.log(data / data.shift(1)).dropna()

# Distribution Analysis
st.subheader("Distribution Analysis")
selected_stock = st.selectbox("Select Stock for Distribution Analysis", options=data.columns)
stock_returns = log_returns[selected_stock]
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(stock_returns, kde=True, ax=ax)
skewness = stock_returns.skew()
kurtosis = stock_returns.kurtosis()
plt.title(f"Distribution of {selected_stock} Returns\nSkewness: {skewness:.2f}, Kurtosis: {kurtosis:.2f}")
st.pyplot(fig)

# Autocorrelation Analysis
st.subheader("Autocorrelation Analysis")
fig, ax = plt.subplots(figsize=(10, 6))
plot_acf(data[selected_stock].dropna(), ax=ax)
st.pyplot(fig)

# Correlation Matrix Heatmap
st.subheader("Correlation Matrix Heatmap")
corr_matrix = log_returns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap="coolwarm", center=0, annot=False)
st.pyplot(plt)

# Download Options
st.subheader("Download Data and Figures")
data_csv = data.to_csv().encode('utf-8')
st.download_button("Download Stock Data (CSV)", data=data_csv, file_name='nifty_50_stock_data.csv')

# Download the correlation matrix heatmap
fig_buffer = BytesIO()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap="coolwarm", center=0)
plt.savefig(fig_buffer, format='png')
fig_buffer.seek(0)
st.download_button("Download Heatmap (PNG)", data=fig_buffer, file_name='heatmap.png')
