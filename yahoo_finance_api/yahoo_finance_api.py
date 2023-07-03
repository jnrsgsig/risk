import json
import pprint
from urllib import parse as url_parse

import requests


def test_yhapi():
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols": "AAPL,BTC-USD,EURUSD=X"}
    headers = {
        'x-api-key': x_api_key.api_key_auth,
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    pprint.pprint(response.text)


class YhFinanceApi:
    _base_url = 'https://yfapi.net'
    with open('yh-finance-api-specification.json', encoding='UTF-8') as _f:
        _specification = json.load(_f)

    @classmethod
    @property
    def __doc__(cls):
        return cls._specification

    @classmethod
    def v6_quote(cls):
        url = url_parse.urljoin(cls._base_url, "/v6/finance/quote")
        querystring = {"symbols": "AAPL,BTC-USD,EURUSD=X"}
        headers = {
            'x-api-key': x_api_key.api_key_auth,
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.text


if __name__ == '__main__':
    print(YhFinanceApi.__doc__)
