# Stock Market Analysis

This is a simple yet complete **Stock Market Data Analysis** project prepared for internship portfolio use.
It contains exploratory data analysis (EDA), visualizations, feature engineering, and a small baseline prediction model.

## What is included
- `stock_analysis.ipynb` — Jupyter Notebook with step-by-step analysis and charts.
- `stocks.csv` — The dataset used (copied from the uploaded file).
- `requirements.txt` — Python libraries needed to run the notebook.
- `summary_report.txt` — Short summary of findings and insights.
- `README.md` — This file.

## Goals
1. Clean and explore the stock data.
2. Visualize price trends, moving averages, returns, and volume patterns.
3. Compute correlations and seasonality (if applicable).
4. Create simple features and build a baseline model to predict next-day Close price using Linear Regression.
5. Provide clear explanations so a reviewer (internship interviewer) can follow your thought process.

## How to run
1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate       # Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook:
   ```bash
   jupyter notebook stock_analysis.ipynb
   ```
4. Run cells in order.

## Notes
- The notebook is written to be clear and teachable for an internship demonstration.
- Replace `stocks.csv` with any other stock dataset (with Date, Open, High, Low, Close, Volume) and the notebook will adapt.
