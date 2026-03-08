import pandas as pd

def trend_score(prices):

    series = pd.Series(prices)

    ema20 = series.ewm(span=20).mean().iloc[-1]

    ema50 = series.ewm(span=50).mean().iloc[-1]

    if ema20 > ema50:
        return 1
    else:
        return -1
