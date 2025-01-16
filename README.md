# Nifty 50 Stock Analysis Dashboard (2023)

This project is a **Streamlit-based web application** that provides a comprehensive analysis of selected Nifty 50 stocks for the year 2023. The dashboard incorporates various features such as data visualization, statistical analysis, and download options to make it easier for users to explore and analyze stock market trends.

---

## Features

### 1. **Stock Price Data**
- Fetches historical stock prices for selected Nifty 50 companies using `yfinance`.
- Allows users to filter stocks by sector (e.g., Energy, Technology, Banking) or view all available stocks.
- Displays stock price data in an interactive table.

### 2. **Interactive Visualizations**
- **Time Series Plot**: Visualize daily adjusted closing prices of selected stocks over time.
- **Distribution Analysis**: Analyze the distribution of log returns for individual stocks, including skewness and kurtosis.
- **Autocorrelation Analysis**: Examine the autocorrelation of stock prices to identify patterns in the time series data.
- **Correlation Matrix Heatmap**: Visualize the correlation between log returns of selected stocks.

### 3. **Data Analysis**
- Calculates **log returns** to understand the percentage change in stock prices.
- Computes a **correlation matrix** for the selected stocks to analyze interdependencies.

### 4. **Download Options**
- Export stock price data as a CSV file.
- Download the correlation matrix heatmap as a PNG image.

---

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
    https://github.com/Harshita-Rupani29/Nifty50_DashBoard.git
    cd nifty50-stock-analysis
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Launch the application**: After running the above command, the app will open in your default web browser.
2. **Select a sector**: Use the sidebar to choose a sector or view all stocks.
3. **Analyze stocks**: Select specific stocks for detailed analysis.
4. **Download results**: Save the stock data and visualizations for offline use.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and analysis.
- **yfinance**: For fetching stock market data.
- **Seaborn & Matplotlib**: For data visualization.
- **Scikit-learn**: For clustering and statistical analysis.
- **Statsmodels**: For time series analysis.


## Future Enhancements

- Add support for additional technical indicators (e.g., RSI, MACD).
- Enable stock comparison across different indices (e.g., Sensex, Dow Jones).
- Implement predictive modeling using machine learning for stock price forecasting.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **yfinance** for providing seamless stock market data.
- **Streamlit** for enabling rapid development of interactive dashboards.
- **Seaborn** and **Matplotlib** for their powerful data visualization tools.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or suggestions.

---

Feel free to replace `your-username` in the GitHub URL with your actual GitHub username before publishing.
