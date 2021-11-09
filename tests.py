import requests


def test_get_all_drinks():
    response = requests.get("http://127.0.0.1:5000/drinks")
    assert response.status_code == 200


def test_get_all_pizzas():
    response = requests.get("http://127.0.0.1:5000/pizzas")
    assert response.status_code == 200


def test_get_all_desserts():
    response = requests.get("http://127.0.0.1:5000/desserts")
    assert response.status_code == 200


def test_get_drink_name_by_id():
    response = requests.get("http://127.0.0.1:5000/drinks/2055844")
    obj_data = response.json()
    assert obj_data["name"] == "mineral water"


def test_get_pizza_name_by_id():
    response = requests.get("http://127.0.0.1:5000/pizzas/2055830")
    obj_data = response.json()
    print(obj_data)
    assert obj_data["name"] == "Margarita"


def test_get_dessert_name_by_id():
    response = requests.get("http://127.0.0.1:5000/desserts/2055836")
    obj_data = response.json()
    print(obj_data)
    assert str(obj_data["price"]) == "29"



