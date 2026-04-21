from api import get_data, headers
from parser import parse_restaurants_data
from display import display_restaurants_to_console

# TODO: Improve: Instead of console display, console application or web interface for the visualization
# TODO: Improve: Postcode can be given as argument by user.
# TODO: Improve: Top_n complete entries are returned. Skip the incomplete data entry.
def main():
    base_url = "https://uk.api.just-eat.io/discovery/"
    postcode = "L4 0TH"
    postcode_no_space = postcode.replace(" ", "")
    endpoint = f"uk/restaurants/enriched/bypostcode/{postcode_no_space}"
    endpoint_url = base_url + endpoint

    data = get_data(endpoint_url=endpoint_url, headers=headers)
    restaurants_list = parse_restaurants_data(data=data, top_n=10)
    display_restaurants_to_console(restaurants_list=restaurants_list)

if __name__ == "__main__":
    main()