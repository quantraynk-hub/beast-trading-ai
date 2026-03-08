def calculate_pcr(option_data):

    if option_data is None:
        return None

    if "records" not in option_data:
        return None

    if "data" not in option_data["records"]:
        return None

    total_put = 0
    total_call = 0

    for item in option_data["records"]["data"]:

        if "CE" in item and "PE" in item:

            total_call += item["CE"]["openInterest"]
            total_put += item["PE"]["openInterest"]

    if total_call == 0:
        return None

    pcr = total_put / total_call

    return round(pcr, 3)
