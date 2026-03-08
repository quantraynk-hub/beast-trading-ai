import requests

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br"
}

session.headers.update(headers)


def get_nifty_price():

    try:
        url = "https://www.nseindia.com/api/allIndices"
        r = session.get(url)
        data = r.json()

        for item in data["data"]:
            if item["index"] == "NIFTY 50":
                return item["last"]

    except:
        return None


def get_option_chain():

    try:
        # first request generates cookies
        session.get("https://www.nseindia.com")

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

        r = session.get(url)

        return r.json()

    except:
        return None
