import requests

from requests_url import make_url_class
import pandas as pd
import json

if __name__ == '__main__':
    ProfileUrl = make_url_class('sc2/legacy/profile/:regionId/:realmId/:profileId/ladders')
    pu = ProfileUrl(regionId=1, realmId=1, profileId=10400261)
    url = pu.requests_url
    print(url)

    content = requests.get(url).content.decode('utf-8')
    content_dict = json.loads(content)
    print(content_dict)
