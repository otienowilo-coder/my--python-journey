import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

#FETCHING EXCHANGE RATES FROM API
def get_exchange_rates(base_currency):
    try:
        response = requests.get(f"{API_URL}{base_currency}")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    rate = rates[to_currency]
    return amount * rate
print(convert_currency(100, 'USD', 'EUR'))
  

 