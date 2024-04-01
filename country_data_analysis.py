import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_country_data()

    def fetch_country_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    def display_home_info(self):
        homes = {}
        currencies = {}
        currency_symbols = {}
        for country in self.data:
            country_name = country.get("name", "N/A")
            homes[country_name] = country.get("flags", {}).get("png", "N/A")
            for currency_code, currency_info in country.get("currencies", {}).items():
                if currency_code not in currencies:
                    currencies[currency_code] = []
                currencies[currency_code].append(country_name)
                currency_symbols[currency_code] = currency_info.get("symbol", "N/A")
        
        print("Homes of Countries:")
        for country, home in homes.items():
            print(f"{country}: {home}")

        print("\nCurrencies:")
        for currency_code, countries in currencies.items():
            print(f"{currency_code}:")
            for country in countries:
                print(f"\t{country}")

        print("\nCurrency Symbols:")
        for currency_code, symbol in currency_symbols.items():
            print(f"{currency_code}: {symbol}")

    def display_countries_with_currency(self, currency_code):
        print(f"Countries with {currency_code} currency:")
        for country in self.data:
            country_name = country.get("name", "N/A")
            for code in country.get("currencies", {}):
                if code == currency_code:
                    print(country_name)


def main():
    url = "https://restcountries.com/v3.1/all"
    country_data = CountryData(url)
    country_data.display_home_info()
    print("\n")
    country_data.display_countries_with_currency("USD")  # Display countries with dollar as currency
    print("\n")
    country_data.display_countries_with_currency("EUR")  # Display countries with euro as currency

if __name__ == "__main__":
    main()
