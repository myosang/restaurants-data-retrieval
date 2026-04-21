from rich.table import Table
from rich.console import Console

def display_restaurants_to_console(restaurants_list: list):
    console = Console()
    table = Table(title="First 10 Restaurants")

    table.add_column("Name")
    table.add_column("Cuisines")
    table.add_column("Rating")
    table.add_column("Address")

    for r in restaurants_list:
        table.add_row(
            r["name"],
            r["cuisines"],
            str(r["rating"]) if r["rating"] is not None else "N/A",
            r["address"]
        )

    console.print(table)

