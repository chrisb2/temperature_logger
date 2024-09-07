"""Thingspeak upload."""
from retrier import retry
import requests
import secrets

_URL = (
    'https://api.thingspeak.com/update.json'
    '?api_key={key}&field1={f1}')


@retry(Exception, tries=5, delay=2, backoff=2.0)
def send(temperature):
    print('Sending...')
    url = _URL.format(key=secrets.THINGSPEAK_API_KEY, f1=temperature)
    with requests.get(url) as response:
        if response.status_code != 200:
            raise ValueError("HTTP status %d" % response.status_code)
        print('Done')
