import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from src.fixtures.api_fixture import api_client


@pytest.mark.api
def test_get_post_by_id(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200, "GET /posts/1 should return 200"
    payload = response.json()
    assert payload["id"] == 1, "Post id should be 1"


@pytest.mark.api
def test_create_post(api_client):
    body = {
        "title": "rest integration",
        "body": "sample payload",
        "userId": 1,
    }

    response = api_client.post("/posts", json=body)

    assert response.status_code == 201, "POST /posts should return 201"
    payload = response.json()
    assert payload["title"] == body["title"], "Created post title should match request"