# dss.py
# Decision Support System: Sales Forecasting using Moving Average & Trendline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# ------------------- INPUT DATA TABLE -------------------
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales_Revenue': [120000, 135000, 130000, 148000, 155000, 170000, 165000, 180000, 195000, 210000, 205000, 220000]
}

df = pd.DataFrame(data)
df['Month_Num'] = range(1, 13)

print("INPUT DATA TABLE")
print("="*50)
print(df[['Month', 'Sales_Revenue']])
print()

# ------------------- MODEL / RULE -------------------
# 1. 3-Month Moving Average
df['3M_MA'] = df['Sales_Revenue'].rolling(window=3).mean()

# 2. Linear Trendline (Simple Regression)
x = df['Month_Num']
y = df['Sales_Revenue']
coefficients = np.polyfit(x, y, 1)  # Slope, Intercept
slope, intercept = coefficients
df['Trendline'] = slope * x + intercept

# Forecast next month (Month 13)
next_month = 13
forecast_ma = df['3M_MA'].iloc[-1]  # Last moving average
forecast_trend = slope * next_month + intercept

print("MODEL USED")
print("="*50)
print(f"1. 3-Month Moving Average: Last 3 months → {forecast_ma:,.0f}")
print(f"2. Linear Trendline: y = {slope:,.0f}x + {intercept:,.0f} → {forecast_trend:,.0f}")
print()

# ------------------- RECOMMENDATION OUTPUT -------------------
avg_forecast = (forecast_ma + forecast_trend) / 2

print("RECOMMENDATION OUTPUT")
print("="*50)
print(f"Predicted Revenue for January (Next Month): ${avg_forecast:,.0f}")
if avg_forecast > df['Sales_Revenue'].mean():
    print("Recommendation: INCREASE inventory and marketing budget.")
else:
    print("Recommendation: Maintain current levels; monitor closely.")
print()

# ------------------- VISUALIZATION -------------------
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales_Revenue'], 'o-', label='Actual Sales', color='blue')
plt.plot(df['Month'], df['3M_MA'], '--', label='3-Month MA', color='orange')
plt.plot(df['Month'], df['Trendline'], ':', label='Trendline', color='green')
plt.axhline(y=avg_forecast, color='red', linestyle='-', label=f'Next Month Forecast: ${avg_forecast:,.0f}')
plt.title('Sales Forecasting Decision Support System')
plt.ylabel('Revenue ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dss_sales_forecast.png', dpi=200)
plt.show()
