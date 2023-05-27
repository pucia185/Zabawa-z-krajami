import requests

def fetch_currency_rates():
    url = f"http://api.nbp.pl/api/exchangerates/tables/A"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_time_currency_rates(start_date, end_date):
    url = f"http://api.nbp.pl/api/exchangerates/tables/A/{start_date}/{end_date}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
