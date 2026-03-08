def calculate_pcr(option_data):

    total_put = 0
    total_call = 0

    for item in option_data["records"]["data"]:

        if "CE" in item and "PE" in item:

            total_call += item["CE"]["openInterest"]
            total_put += item["PE"]["openInterest"]

    pcr = total_put / total_call

    return pcr
