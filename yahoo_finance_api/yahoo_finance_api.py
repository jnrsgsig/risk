import pprint

import requests

import x_api_key


def test_yhapi():
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols": "AAPL,BTC-USD,EURUSD=X"}
    headers = {
        'x-api-key': x_api_key.my_personal_api_key,
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    pprint.pprint(response.text)
