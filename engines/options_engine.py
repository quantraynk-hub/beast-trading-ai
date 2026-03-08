def calculate_pcr(option_data):

    # API failed
    if option_data is None:
        return None

    # API returned unexpected type
    if not isinstance(option_data, dict):
        return None

    # Missing keys
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

    pcr = total_put / total_call

    return round(pcr, 3)
