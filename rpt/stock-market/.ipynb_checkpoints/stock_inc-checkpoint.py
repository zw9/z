import glob, os
import sqlite3

sqlitedb = sqlite3.connect('stock_db.sqlite')
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interactive
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = (dt.date.today() + dt.timedelta(days=-10))
# dt.datetime(2018,6,1)
end = dt.datetime.now()
yesterday = (dt.date.today() + dt.timedelta(days=-1)).strftime('%Y%m%d')
yesterday
today = (dt.date.today() + dt.timedelta(days=0)).strftime('%Y%m%d')
today
tomorrow = (dt.date.today() + dt.timedelta(days=1)).strftime('%Y%m%d')
tomorrow
import glob


# https://amigobulls.com/stocks/ABMD/historical-stock-prices
# http://www.eoddata.com/download.aspx


# ,"AET","ALGN","AVGO","BA","BOX","BZUN","EVBG","GERN","HAE","HTHT","HUM","LH","LOXO","MA","MDB","MKSI","MOH","MOMO","MSFT","MSG","NFLX","PYPL","SQ","THC","TWTR","UNH","WDC","WWE"]


def fnc_fetch_one(ticker='UNH', src='morningstar', xxstart=start, xxend=end):
    global df_fetch_one
    df_fetch_one = web.DataReader(ticker, src, xxstart, xxend)
    df_fetch_one.reset_index(level=['Symbol', 'Date'], inplace=True)
    df_fetch_one.sort_values(by=['Symbol', 'Date'], inplace=True, ascending=[True, False])
    df_fetch_one['Low_High_pct'] = (df_fetch_one['High'] - df_fetch_one['Low']) / df_fetch_one['Low']
    df_fetch_one['Open_Close_pct'] = (df_fetch_one['Close'] - df_fetch_one['Open']) / df_fetch_one['Close']
    df_fetch_one['High_Close_pct'] = (df_fetch_one['High'] - df_fetch_one['Close']) / df_fetch_one['Close']
    df_fetch_one['VolxClose'] = df_fetch_one['Close'] * df_fetch_one['Volume'] / 1000000
    df_fetch_one['VolxClose_pct'] = ((df_fetch_one['VolxClose'] / df_fetch_one['VolxClose'].shift(-1)) - 1).fillna(0)
    df_fetch_one['1m_chg'] = ((df_fetch_one['Close'] - df_fetch_one['Close'].shift(-1))).fillna(0)
    df_fetch_one['1m_pct'] = ((df_fetch_one['1m_chg'] / df_fetch_one['Close'].shift(-1))).fillna(0)
    df_fetch_one['1m_pct'] = df_fetch_one['1m_pct'].abs()
    df_fetch_one = df_fetch_one.ix[df_fetch_one['Date'] > df_fetch_one['Date'].min()]
    df_fetch_one.to_sql(src, sqlitedb, if_exists="replace")
    return df_fetch_one[:10];


def show_stock(src='morningstar'):
    rpt = pd.read_sql("select * from " + src, sqlitedb)
    rpt = rpt.drop(rpt.columns[[4, 5, 6]], axis=1)
    rpt1 = rpt.sort_values(['1m_pct'], ascending=[False], inplace=False)
    output = rpt1.to_string(formatters={
        'Close': '{:,.0f}'.format,
        'High': '{:,.0f}'.format,
        'Low': '{:,.0f}'.format,
        'Open': '{:,.0f}'.format,
        'Volume': '{:,.0f}'.format,
        'Low_High_pct': '{:,.0%}'.format,
        'Open_Close_pct': '{:,.0%}'.format,
        'High_Close_pct': '{:,.0%}'.format,
        '1m_pct': '{:,.0%}'.format,
        'VolxClose_pct': '{:,.0%}'.format,
        'VolxClose': '{:,.0f}'.format})
    print(output)


def eoddata_ticker(xx_ticker='ABMD'):
    global df_fetch_one
    rpt = df_fetch_one.ix[df_fetch_one['Symbol'] == xx_ticker][:20]
    rpt = rpt.drop(rpt.columns[[3, 4, 5, 6]], axis=1)
    rpt1 = rpt.sort_values(['1m_pct'], ascending=[False], inplace=False)
    output = rpt1.to_string(formatters={
        'Close': '{:,.0f}'.format,
        'High': '{:,.0f}'.format,
        'Low': '{:,.0f}'.format,
        'Open': '{:,.0f}'.format,
        'Volume': '{:,.0f}'.format,
        'Low_High_pct': '{:,.0%}'.format,
        'Open_Close_pct': '{:,.0%}'.format,
        'High_Close_pct': '{:,.0%}'.format,
        '1m_pct': '{:,.0%}'.format,
        'VolxClose_pct': '{:,.0%}'.format,
        'VolxClose': '{:,.0f}'.format})
    print(output)


def do_import_one(nm='commercial', fullname='fullname', xx_sep=","):
    nm = nm.lower()
    df = pd.read_csv(fullname, sep=xx_sep)
    df.to_sql(nm, sqlitedb, if_exists="replace")


def do_filesearch(srchtxt='/home/b4gone/Dropbox/csv/*.csv', xx_sep=","):
    for name in glob.glob(srchtxt):
        display(os.path.basename(name).split('.')[0])
        do_import_one(nm=os.path.basename(name).split('.')[0], fullname=name, xx_sep=xx_sep)

    # df_fetch_one=df_fetch_one.ix[df_fetch_one['Date'] > '2018-06-01']


def do_use(src='USE_20180102'):
    df = show_df(src=src)
    df['Low_High_pct'] = round(((df['<high>'] - df['<low>']) / df['<low>']).abs() * 100, 1)
    df['VolxClose'] = round(df['<close>'] * df['<vol>'] / 1000000, 1)
    df = df[df['<open>'] > 100]
    df.sort_values(by=['Low_High_pct'], inplace=True, ascending=False)
    display(df[:10])


def show_df(src='USE_20180102'):
    rpt = pd.read_sql("select * from " + src, sqlitedb)
    return rpt;

# fnc_fetch_one(ticker=csvs,src='robinhood')
#    display(df_fetch_one)
# .sort_values(ascending=False, by='Close')
#   df_fetch_one=df_fetch_one.ix[df_fetch_one['Date'] > 20180102]
#    df_fetch_one['Rank'] = df_fetch_one.groupby(['Symbol'])['Date'].rank(ascending=False)
#    df_fetch_one=df_fetch_one.ix[df_fetch_one['VolxClose'] > 10.0].round(2)
#    display(df_fetch_one[df_fetch_one['Date'].str.endswith(df_fetch_one['Date'].max()[-2:])].round(2)[:5]);
#    display(df_fetch_one)

# df_nasdaq_symbols=pandas_datareader.nasdaq_trader.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)
# display(df_nasdaq_symbols[:10])
# !python3 -m pip install pylab --user
# !python3 -m pip install matplotlib --user
# !python3 -m pip install jupyter_dashboards --user
# !jupyter dashboards quick-setup --sys-prefix

# !python3 -m pip install pandas --user
# !python3 -m pip install pandas-datareader --user
# !python3 -m pip install yahoo_finance_historical_data_extract --user
# !python3 -m pip install ipywidgets
# !jupyter nbextension enable --py widgetsnbextension

# !ls -l /home/b4gone/Downloads/**
# !ls -l /home/b4gone/Downloads/**.zip
# !unzip -o /home/b4gone/Downloads/*.zip  
# !rm /home/b4gone/Downloads/*.zip  
# !head /home/b4gone/Downloads/NASDAQ_20180*.txt
# !head  /home/b4gone/Dropbox/csv/UNH_20180601.csv
# * [http://www.eoddata.com/download.aspx](http://www.eoddata.com/download.aspx)

# !mv ~/Downloads/*.csv ~/Dropbox/csv/
# !mv ~/Downloads/USE*.txt ~/Dropbox/txt/

# !rm `ls  ~/Dropbox/csv/*\(*\).csv`
# !rm `ls  ~/Dropbox/csv/*30.csv`
# !ls ~/Dropbox/csv/*.csv
# !ls ~/Dropbox/txt/USE*
# !xed ~/Dropbox/py/stock_inc.py

# !python3 -m pip install jupyter_dashboards
# !jupyter dashboards quick-setup --user
#    display(df_fetch_one.columns)
#   display(df_fetch_one.index)
#    df_fetch_one.reset_index() 
#    df_fetch_one=df_fetch_one.stack(level=0).reset_index()
#    df_fetch_one=pd.melt(df_fetch_one)
# .drop('level_0', axis=1)
#    display(df_fetch_one.columns)
#    display(df_fetch_one.index)
#    display('df_fetch_one')
#   display(df_fetch_one[df_fetch_one.index['Date']])
# Index(['Close', 'High', 'Low', 'Open', 'Volume'], dtype='object')
#   df_fetch_one['Low_High_chg']=df_fetch_one['High'] -df_fetch_one['Low'] 
# df_fetch_one.sort_index(inplace=True,ascending=[True, False])
#    df_fetch_one= pandas_datareader.mstar.daily.MorningstarDailyReader(ticker, start=xxstart, end=xxend, retry_count=3, pause=0.1, timeout=30, session=None, freq=None, incl_splits=False, incl_dividends=False, incl_volume=True, currency='usd', interval='d')
#    display(df_fetch_one)
# df_fetch_one=df_fetch_one.ix[df_fetch_one['1m_pct'] > 0.01]

#    display(df_fetch_one.columns)
#    stkmove=df_fetch_one.sort_values(['1m_pct'], ascending=[False], inplace=False)
#    display(stkmove)
