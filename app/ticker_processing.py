
from app import app
import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show

base_url = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?"
auth = f"&api_key={app.config['QUANDL_KEY']}"

def load_ticker(ticker="GOOG"):
    req = base_url+f"ticker={ticker}"+auth
    r = requests.get(req)
    return r.json()


def preprocess_json(raw_dict):
    raw_dict = raw_dict['datatable']
    data = raw_dict['data']
    columns = raw_dict['columns']
    # list of tables and a list of strings
    return data, [col['name'] for col in columns]


def ticker_df(ticker):
    data, cols = preprocess_json(load_ticker(ticker))
    stock = pd.DataFrame(data,columns = cols)
    stock['date'] = pd.to_datetime(stock['date'])
    return stock
