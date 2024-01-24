import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
foods = []

def test_create_food():
    """test for creating food in db"""
    new_food_data = {
        "name": "Banana da terra",
        "description": "A yellow fruit with a peel from earth power",
        "calories": 105,
        "time": "2023-01-05T10:15:32",
        "diet": True
    }
    response = requests.post(f"{BASE_URL}/food", json=new_food_data, timeout=5)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "food_id" in response_json 
    foods.append(response_json["food_id"])

def test_get_foods():
    """test for geting all food list"""
    response = requests.get(f"{BASE_URL}/food", timeout=5)
    assert response.status_code == 200

def test_get_food():
    """test for geting a specific food"""
    if foods:
        food_id = foods[0]
        response = requests.get(f"{BASE_URL}/food/{food_id}", timeout=5)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == food_id

def test_update_food():
    """test for updating a specific food"""
    if foods:
        food_id = foods[0]
        payload = {
            "name": "Comida atualizada",
            "diet": False
        }

        response = requests.put(f"{BASE_URL}/food/{food_id}", json=payload, timeout=5)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

def test_delete_food():
    """test for geting a specific food"""
    if foods:
        food_id = foods[0]
        response = requests.delete(f"{BASE_URL}/food/{food_id}", timeout=5)
        assert response.status_code == 200
        response = requests.get(f"{BASE_URL}/food/{food_id}", timeout=5)
        assert response.status_code == 404