import api
from unittest.mock import Mock
import pytest

# Isolate the environment (no internet) and test fast and predictable
# Test with Mock
def test_get_data_return_json(monkeypatch: pytest.MonkeyPatch):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "restaurant": []
    }
    # Define the fake 'get' request for later.
    mock_get = Mock(return_value=mock_response)

    monkeypatch.setattr(api.requests, "get", mock_get)

    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
    headers = api.headers

    result = api.get_data(endpoint_url=url, headers=headers)

    assert result == {
        "restaurant": []
    }

