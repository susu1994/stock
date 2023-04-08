import yfinance as yf
import pandas as pd
msft = yf.Ticker("VZ")
df = pd.DataFrame(msft.history(period="3mo"))
df_new = df.reset_index(inplace=False)
df_new['Date'] = pd.to_datetime(df_new['Date']).dt.date
df_new = df_new[["Date","Close"]]
df_new.to_excel("2.xlsx")
# Let us  get historical stock prices for Facebook
# covering the past few years.
# max->maximum number of daily prices available
# for Facebook.
# Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y,
# 5y, 10y and ytd.
# print(df_new.dtypes)