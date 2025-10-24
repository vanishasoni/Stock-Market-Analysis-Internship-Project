# simple_data_analysis.py
# A lightweight script to compute basic stats from stocks.csv
import pandas as pd
df = pd.read_csv('stocks.csv')
print('Shape:', df.shape)
print('Columns:', df.columns.tolist())
if 'Close' in df.columns:
    print('Latest Close:', df['Close'].iloc[-1])
