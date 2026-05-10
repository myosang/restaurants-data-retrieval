from display import display_restaurants_to_console
from io import StringIO
from rich.console import Console

def test_display_restaurants_to_console():
    buffer = StringIO()
    console = Console(
        file = buffer,
        force_terminal=False,
        color_system=None,
        width=120
    )

    mock_restaurants_list = [{
        "name": "Test Restaurant",
        "cuisines": "Burger, Pizza, Salad",
        "rating": 5.0,
        "address": "liverpool"
    }]
    
    display_restaurants_to_console(mock_restaurants_list, console=console)

    output = buffer.getvalue()

    assert "Test Restaurant" in output
    assert "5.0" in output
