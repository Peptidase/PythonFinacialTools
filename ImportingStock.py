# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:24:23 2021

@author: ArifM
this uses the Intro and getting stock price data - 
Python programming for finance tutorial series

"""

import datetime as dt
import pandas as pd
import pandas_datareader as web 
#Lets you use various datasources from online
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
style.use('ggplot')

start = dt.datetime(2019,1,1)
end = dt.datetime(2021, 1, 10)

df = web.DataReader('TSLA','yahoo',start,end)# Daily data,

df_ohlc = df['Adj Close'].resample('10D').ohlc() #open high low close
df_volume = df['Volume'].resample('10D').sum()

fig, ax = plt.subplots()

mpf.plot(df_ohlc, type='candle',mav = (10,50,100))

df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df.dropna(inplace=True) # removes the rows that have nan
#TODO Create a subplot of volume below the candlestick graph that is coloured.
