import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

#FETCHING EXCHANGE RATES FROM API
def get_exchange_rates(base_currency):
    
    try:
        response = requests.get(f"{API_URL}{base_currency}", timeout=10)  # Set a timeout of 10 seconds
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    rates = get_exchange_rates(from_currency)
    if rates is None:
        print("Failed to retrieve exchange rates.")
        return None
    try:
         rate = rates[to_currency]  
    except KeyError as e:
       print(f"Unknown currency input: {e}")
       return None

    return amount * rate
    amount = (float(input("Enter the amount to convert: ")))
    print(amount)
    #print(type(amount))
    input_currency = input("Enter the currency to convert from (e.g., usd or eur): ")
    output_currency = input("Enter the currency to convert to (e.g., gbp or jpy): ")


amount = (float(input("Enter the amount to convert: ")))
input_currency = input("Enter the currency to convert from (e.g., usd or eur): ")
output_currency = input("Enter the currency to convert to (e.g., gbp or jpy): ")
print(convert_currency(amount, input_currency, output_currency))