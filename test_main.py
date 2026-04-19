from main import parse_restaurants_data

def test_parse_restaurants_data_basic():
    mock_data = {
        "restaurants": [
            {
                "name": "McDonald's® - Walton Rd",
                "cuisines": [
                        {"name": "Burgers", "uniqueName": "burgers"},
                        {"name": "Chicken", "uniqueName": "chicken"},
                        {"name": "Breakfast", "uniqueName": "breakfast"},
                        {"name": "Sandwiches", "uniqueName": "sandwiches"},
                        {"name": "Deals", "uniqueName": "deals"},
                        {"name": "Freebies", "uniqueName": "freebies"}
                    ],
                "rating": {"count": 13763, "starRating": 3, "userRating": None},
                "address": {
                        "city": "Liverpool",
                        "firstLine": "202/218 Walton Road",
                        "postalCode": "L4 4BB",
                        "location": {"type": "Point", "coordinates": [-2.97211, 53.436737]}
                    },
            }
        ]
    }
    result = parse_restaurants_data(mock_data, 10)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "McDonald's® - Walton Rd"
    assert result[0]["cuisines"] == "Burgers, Chicken, Breakfast, Sandwiches, Deals, Freebies"
    assert result[0]["rating"] == 3
    assert result[0]["address"] == "202/218 Walton Road, Liverpool"

def test_parse_restaurants_data_missing_fields():
    mock_data = {
        "restaurants": [
            {
                "name": "Unknown",
                "cuisines": [],
                "rating": {},
                "address": {}
            }
        ]
    }
    result = parse_restaurants_data(mock_data, 10)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "Unknown"
    assert result[0]["cuisines"] == ""
    assert result[0]["rating"] == ""
    assert result[0]["address"] == ", "

def test_parse_restaurants_data_limit():
    mock_data = {
        "restaurants": [
            {"name": f"restaurant {i}"} for i in range(30)
        ]
    }
    result = parse_restaurants_data(mock_data, 10)
    
    assert isinstance(result, list)
    assert len(result) == 10