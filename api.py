import requests

# Headers used in the Take it away UK restaurants endpoint
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.just-eat.co.uk/"
}

def get_data(endpoint_url: str, headers: dict):
    response = requests.get(url=endpoint_url, headers=headers)
    return response.json()