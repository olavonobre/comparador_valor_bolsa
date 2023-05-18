import yfinance as yf
from datetime import datetime

def get_ticker_symbol(company_name):
    tickerData = yf.Ticker(company_name)
    info = tickerData.info
    return info['symbol']

def get_stock_price(tickerSymbol):
    today = datetime.today().strftime('%Y-%m-%d')
    tickerData = yf.Ticker(tickerSymbol)
    tickerDF = tickerData.history(period='1d', start='2010-1-1', end=today)
    current_price = tickerDF["Close"].iloc[-1]
    return current_price

company_name = input('Digite o nome da ação: ')
tickerSymbol = get_ticker_symbol(company_name)
current_price = get_stock_price(tickerSymbol)

if current_price < 24:
    print(f"O preço atual da ação {tickerSymbol} é {current_price:.2f} e está abaixo de R$24.")
else:
    print(f"O preço atual da ação {tickerSymbol} é {current_price:.2f}.")

