import requests


def get_info(url):
    data = requests.get(url)
    print(data.status_code)
    return data
