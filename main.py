import requests
import json
import pandas as pd

# Headers used in the Take it away UK restaurants endpoint
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.just-eat.co.uk/"
}

# Get data from endpoint
def get_data(endpoint_url: str, headers: dict):
    response = requests.get(url=endpoint_url, headers=headers)
    return response.json()

# Parse top N data
def parse_restaurants_data(data: list[dict], top_n: int):
    # TODO: Improve: Top_n complete entries are returned. Skip the incomplete data entry.
    # TODO: Improve: Make sure the rating is returned as number.
    restaurants = data["restaurants"][:top_n]
    restaurants_list = []
    for r in restaurants:
        name = r.get("name")
        cuisines = ", ".join(c["name"] for c in r.get("cuisines", []))
        rating = r.get("rating", {}).get("starRating", "")
        address_obj = r.get("address", {})
        address = f"{address_obj.get('firstLine', '')}, {address_obj.get('city', '')}"
        restaurants_list.append({
            "name": name,
            "cuisines": cuisines,
            "rating": rating,
            "address": address
        })
    return restaurants_list

if __name__ == "__main__":
    base_url = "https://uk.api.just-eat.io/discovery/"
    # TODO: Improve: Postcode can be given as argument by user.
    postcode = "L4 0TH"
    postcode_no_space = postcode.replace(" ", "")
    endpoint = f"uk/restaurants/enriched/bypostcode/{postcode_no_space}"
    endpoint_url = base_url + endpoint

    data = get_data(endpoint_url=endpoint_url, headers=headers)
    restaurants_list = parse_restaurants_data(data=data, top_n=10)
    restaurants_df = pd.DataFrame(restaurants_list)
    # TODO: Improve: user friendly display of the data.
    print(restaurants_df)
