def generate_signal(trend, pcr):

    if trend == 1 and pcr > 1.1:
        return "BUY CE"

    if trend == -1 and pcr < 0.9:
        return "BUY PE"

    return "WAIT"
