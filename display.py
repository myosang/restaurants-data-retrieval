from rich.table import Table
from rich.console import Console

def display_restaurants_to_console(restaurants_list: list):
    console = Console()
    table = Table(title="First 10 Restaurants")

    table.add_column("name")
    table.add_column("cuisines")
    table.add_column("rating")
    table.add_column("address")

    for r in restaurants_list:
        table.add_row(
            r["name"],
            r["cuisines"],
            str(r["rating"]),
            r["address"]
        )

    console.print(table)

