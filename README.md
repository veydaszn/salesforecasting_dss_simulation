# salesforecasting_dss_simulation
Sales Forecasting using Moving Average and Trendline
=================================================================
          DECISION SUPPORT SYSTEM: SALES FORECASTING
=================================================================

1. INPUT DATA TABLE
----------------------------------------------------
| Month | Sales_Revenue |
|-------|---------------|
| Jan   | 120,000       |
| Feb   | 135,000       |
| ...   | ...           |
| Dec   | 220,000       |
----------------------------------------------------

2. MODEL / RULE USED
----------------------------------------------------
• 3-Month Moving Average: Smooths short-term fluctuations
• Linear Trendline: y = 8,182x + 118,636 (fitted via least squares)
• Combined Forecast: Average of both methods

3. RESULT & RECOMMENDATION
----------------------------------------------------
Predicted January Revenue: $227,773
Recommendation: INCREASE inventory and marketing budget.
(Above annual average of $169,417)

4. DSS STRUCTURE
----------------------------------------------------
- Input: Historical monthly sales
- Processing: Moving average + regression
- Output: Forecast + actionable recommendation
- Visualization: Chart saved as 'dss_sales_forecast.png'

=================================================================
