import yfinance as yf

def get_nifty_price():

    try:
        ticker = yf.Ticker("^NSEI")
        data = ticker.history(period="1d")

        price = data["Close"].iloc[-1]

        return round(price,2)

    except:
        return None


def get_option_chain():
    return None
