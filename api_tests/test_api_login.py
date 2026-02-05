import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0
    assert "email" in data[0]


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0
    assert "title" in data[0]
