import requests

class BreweryData:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def get_breweries_by_state(self, states):
        breweries_by_state = {}
        for state in states:
            url = f"{self.base_url}?by_state={state}"
            response = requests.get(url)
            if response.status_code == 200:
                breweries = response.json()
                brewery_names = [brewery['name'] for brewery in breweries]
                breweries_by_state[state] = brewery_names
            else:
                print(f"Failed to fetch data for state {state}")
        return breweries_by_state

    def count_breweries_by_state(self, states):
        breweries_count_by_state = {}
        for state in states:
            url = f"{self.base_url}?by_state={state}"
            response = requests.get(url)
            if response.status_code == 200:
                breweries = response.json()
                breweries_count_by_state[state] = len(breweries)
            else:
                print(f"Failed to fetch data for state {state}")
        return breweries_count_by_state

    def count_brewery_types_by_city(self, states):
        brewery_types_count_by_city = {}
        for state in states:
            url = f"{self.base_url}?by_state={state}"
            response = requests.get(url)
            if response.status_code == 200:
                breweries = response.json()
                for brewery in breweries:
                    city = brewery['city']
                    brewery_type = brewery['brewery_type']
                    if city not in brewery_types_count_by_city:
                        brewery_types_count_by_city[city] = {}
                    if brewery_type not in brewery_types_count_by_city[city]:
                        brewery_types_count_by_city[city][brewery_type] = 1
                    else:
                        brewery_types_count_by_city[city][brewery_type] += 1
            else:
                print(f"Failed to fetch data for state {state}")
        return brewery_types_count_by_city

    def count_breweries_with_websites_by_state(self, states):
        breweries_with_websites_by_state = {}
        for state in states:
            url = f"{self.base_url}?by_state={state}&has_website=true"
            response = requests.get(url)
            if response.status_code == 200:
                breweries_with_websites = response.json()
                breweries_with_websites_by_state[state] = len(breweries_with_websites)
            else:
                print(f"Failed to fetch data for state {state}")
        return breweries_with_websites_by_state

def main():
    states = ["Alaska", "Maine", "New York"]
    brewery_data = BreweryData()

    # Task 1: List names of breweries in specified states
    breweries_by_state = brewery_data.get_breweries_by_state(states)
    print("Breweries in Alaska, Maine, and New York:")
    for state, breweries in breweries_by_state.items():
        print(f"\n{state}:")
        for brewery in breweries:
            print(brewery)

    # Task 2: Count of breweries in each state
    breweries_count_by_state = brewery_data.count_breweries_by_state(states)
    print("\nCount of Breweries in Alaska, Maine, and New York:")
    for state, count in breweries_count_by_state.items():
        print(f"{state}: {count}")

    # Task 3: Count of brewery types by city
    brewery_types_count_by_city = brewery_data.count_brewery_types_by_city(states)
    print("\nCount of Brewery Types by City:")
    for city, types in brewery_types_count_by_city.items():
        print(f"\n{city}:")
        for type_, count in types.items():
            print(f"{type_}: {count}")

    # Task 4: Count and list of breweries with websites by state
    breweries_with_websites_by_state = brewery_data.count_breweries_with_websites_by_state(states)
    print("\nCount and List of Breweries with Websites in Alaska, Maine, and New York:")
    for state, count in breweries_with_websites_by_state.items():
        print(f"\n{state}:")
        url = f"{brewery_data.base_url}?by_state={state}&has_website=true"
        response = requests.get(url)
        if response.status_code == 200:
            breweries_with_websites = response.json()
            for brewery in breweries_with_websites:
                print(brewery['name'])

if __name__ == "__main__":
    main()

