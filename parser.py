def parse_restaurants_data(data: dict, top_n: int):
    restaurants = data.get("restaurants", [])[:top_n]
    restaurants_list = []
    for r in restaurants:
        name = r.get("name")
        cuisines = ", ".join(c["name"] for c in r.get("cuisines", []))
        rating_raw = r.get("rating", {}).get("starRating")
        rating = float(rating_raw) if rating_raw is not None else None
        address_obj = r.get("address", {}) 
        address = f"{address_obj.get('firstLine', '')}, {address_obj.get('city', '')}"
        restaurants_list.append({
            "name": name,
            "cuisines": cuisines,
            "rating": rating,
            "address": address
        })
    return restaurants_list