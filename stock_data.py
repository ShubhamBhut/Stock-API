import yfinance as yf

def get_data(ticker):
    ticker = yf.Ticker(ticker+".NS")
    data = ticker.history(period="1y")
    opening_prices = data["Open"]
    closing_prices = data["Close"]
    high = data['High']
    low = data['Low']
    volume = data['Volume']

    return {
       'opening_prices': opening_prices,
       'closing_prices': closing_prices,
       'high': high,
       'low': low,	
       'volume': volume	
    }
