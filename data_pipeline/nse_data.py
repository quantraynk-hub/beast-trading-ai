import requests

headers = {"User-Agent": "Mozilla/5.0"}

def get_nifty_price():

    url = "https://www.nseindia.com/api/allIndices"

    r = requests.get(url, headers=headers)

    data = r.json()

    for item in data["data"]:
        if item["index"] == "NIFTY 50":
            return item["last"]


def get_option_chain():

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    r = requests.get(url, headers=headers)

    return r.json()
