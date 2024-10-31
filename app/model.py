import requests

class StarwarsModel:
    API_URL = "https://swapi.dev/api/people"

    @staticmethod
    def fetch_people_data():
        try:
            response = requests.get(StarWarsModel.API_URL)
            response.raise_for_status()
            data = response.json().get("results", [])
            sorted_data = sorted(data, key=lambda x: x.get("name", "").lower())
            return sorted_data
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
