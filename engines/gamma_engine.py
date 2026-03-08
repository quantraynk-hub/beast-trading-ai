def gamma_exposure(option_data):

    gamma = 0

    for item in option_data["records"]["data"]:

        if "CE" in item:

            oi = item["CE"]["openInterest"]

            strike = item["strikePrice"]

            gamma += oi * strike

    return gamma
