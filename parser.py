def parse_restaurants_data(data: dict, top_n: int):
    restaurants = data.get("restaurants", [])
    restaurants_list = []
    for r in restaurants:
        name = r.get("name")
        cuisines = ", ".join(c["name"] for c in r.get("cuisines", []))
        rating_raw = r.get("rating", {}).get("starRating")
        rating = float(rating_raw) if rating_raw is not None else None
        address_obj = r.get("address", {})
        firstLine = address_obj.get("firstLine", "")
        city= address_obj.get("city", "")
        address_parts = [firstLine, city]
        address = ", ".join(part for part in address_parts if part)
        if not address:
            address = "Unknown address"
        restaurants_list.append({
            "name": name,
            "cuisines": cuisines,
            "rating": rating,
            "address": address
        })
    sorted_restaurants_list = sort_restaurants_data(restaurants_list=restaurants_list)[:top_n]
    return sorted_restaurants_list

# Add sorting later
def sort_restaurants_data(restaurants_list: list):
    sorted_list = sorted(
        restaurants_list,
        key=lambda r: r["rating"] if r["rating"] is not None else -1,
        reverse=True
    )
    return sorted_list
