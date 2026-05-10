from api import get_data, headers
from parser import parse_restaurants_data
from display import display_restaurants_to_console
import argparse

def accept_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "postcode",
        help="post code is given by user inside the double quotations",
        type=str
    )
    args = parser.parse_args()
    postcode = args.postcode
    return postcode

def main():
    base_url = "https://uk.api.just-eat.io/discovery/"
    postcode = accept_argument()
    postcode_no_space = postcode.replace(" ", "")
    endpoint = f"uk/restaurants/enriched/bypostcode/{postcode_no_space}"
    endpoint_url = base_url + endpoint
    data = get_data(endpoint_url=endpoint_url, headers=headers)
    restaurants_list = parse_restaurants_data(data=data, top_n=10)
    display_restaurants_to_console(restaurants_list=restaurants_list)

if __name__ == "__main__":
    main()