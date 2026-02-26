import os
import pytest

from src.helpers.api_client import ApiClient


@pytest.fixture(scope="function")
def api_client():
    base_url = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    client = ApiClient(base_url=base_url)
    yield client
    client.close()