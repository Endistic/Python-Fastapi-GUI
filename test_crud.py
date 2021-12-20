from main import app
import requests
import json


# def test_register_member_child():
#     response = clients.post("/api/v1/user/create",json={'id': 1, 'name': "BIG", 'age': 27})
#     print(response.json())


def create_user(name, age, info):
    user_info = {
        'name': name,
        'age': age,
        'info': info
    }
    response = requests.post("http://127.0.0.1:8000/user/create", json=user_info)
    r = response.json()
    print(r)
    return r


def fetch_user():
    response = requests.get("http://127.0.0.1:8000/user/read")
    r = response.json()
    return r


def fetch_userbyId(id):
    data = {
        'id': id
    }
    response = requests.get("http://127.0.0.1:8000/user/getById", params=data)
    r = response.json()
    return r


def edit_user(id, name, age, info):
    user_info = {
        'name': name,
        'age': age,
        'info': info
    }
    response = requests.put("http://127.0.0.1:8000/user/edit/"+id, json=user_info)
    r = response.json()
    return r


def delete_user(id):
    response = requests.delete("http://127.0.0.1:8000/user/delete/" + id, params=id)
    r = response.json()
    print(r)
    return r
