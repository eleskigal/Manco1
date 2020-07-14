import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime as date
#Importaremos las acciones que conforman el DJI
tickers = ["^DJI", "JNJ", "WMT", "KO", "DIS", "RG", "PFE", "HD", "UTX", "VZ", "MRK", "MCD", "WBA", "CVX", "BA", "AAPL", "MMM", "NKE", "UNH", "INTC", "XOM", "IBM", "CAT", "DWDP", "V", "CSCO", "JPM", "GS", "TRV", "MSFT", "AXP" ]
enddate = date.datetime(2019,11,10)
startdate = date.datetime(2019,10,10)
data = pd.DataFrame()
for tick in tickers:
    data[tick] =pdr.get_data_yahoo(tick, start=startdate, end=enddate)["Close"] 
    #con pdr.get importamos los datos de las paginas de internet
print(data.head())