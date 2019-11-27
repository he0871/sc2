import json

import requests
import re


def make_url_class(format: str, ):
    """

    :param base_url: e.g. "sc2/legacy/profile"
    :param format: required_items of required items, seperated by '/', e.g. 'region/realm/profile'
    :return: url class
    """
    host_url = "https://us.api.blizzard.com/"

    class UrlClass(dict):
        token_url = "https://us.battle.net/oauth/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': 'a40d69d0e1554ff49e272d27a451790f',
            'client_secret': '6qtnPOmIEZpXRxw2ZWO8MzozpwkZfPG9',
        }
        required_items = format.split('/')

        @property
        def requests_url(self):
            def translate(name: str):
                if name.startswith(':'):
                    return str(self.get(name.split(":")[1]))
                else:
                    return name

            elements = format.split('/')
            query_url = '/'.join([translate(e) for e in elements])

            return host_url + query_url + f'?access_token={self.token}'

        @property
        def token(self):
            response = requests.post(self.token_url, data=self.payload)
            access_token = json.loads(response.content.decode('utf-8'))['access_token']
            return access_token

    return UrlClass


if __name__ == '__main__':
    profile = 10400261
    region = 1
    realm = 1
    Url = make_url_class('sc2/legacy/profile/:regionID/:realmID/:profileID')
    url = Url(regionID=1, realmID=1, profileID=10400261)
    print(url.requests_url)
