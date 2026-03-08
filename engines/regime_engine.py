import numpy as np

def detect_regime(prices):

    volatility = np.std(prices)

    if volatility > 40:
        return "TRENDING"
    else:
        return "SIDEWAYS"
