def parse_restaurants_data(data: dict, top_n: int):
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