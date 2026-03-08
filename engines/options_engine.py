def calculate_pcr(option_data):

    # API failed
    if option_data is None:
        return None

    # ensure dictionary
    if not isinstance(option_data, dict):
        return None

    records = option_data.get("records")

    if not records:
        return None

    data = records.get("data")

    if not data:
        return None

    total_put = 0
    total_call = 0

    for item in data:

        ce = item.get("CE")
        pe = item.get("PE")

        if ce and pe:
            total_call += ce.get("openInterest", 0)
            total_put += pe.get("openInterest", 0)

    if total_call == 0:
        return None

    return round(total_put / total_call, 3)
