import requests
import pytest

# pytest tests/test_api.py


ENDPOINT = 'http://127.0.0.1:8000/'
pytest.global_variable_JWT_user = ''

'''TEST - User part'''


def test_user_create():
    """ Создание пользователя, не забудьте актививароть пользователя"""

    payload = {
        'name': 'John',
        'surname': 'Snow',
        'email': 'test@mail.ru',
        'password': 'Test007007',
    }

    response = requests.post(ENDPOINT + 'api/clients/create', json=payload)
    # если пользователь не создан вернется код 201, если существует - 400
    try:
        assert response.status_code == 201
        data = response.json()
        return data['id']
    except:
        assert response.status_code == 400


def test_user_get_Jwt():
    """ Получение токена пользователя. НЕ ЗАБУДЬТЕ активировать пользователя, иначе токен не получить """

    payload = {
        'email': 'test@mail.ru',
        'password': 'Test007007',
    }

    response = requests.post(
        f"{ENDPOINT}/auth/jwt/create", json=payload)

    assert response.status_code == 200
    data = response.json()
    print(data)
    print(data['access'])
    pytest.global_variable_JWT_user = data['access']
    return pytest.global_variable_JWT_user


def test_get_list_users():
    """ Получение списка пользователей, используем JWT токен  полученный выше """

    header = {
        'Authorization': 'JWT ' + pytest.global_variable_JWT_user}

    response = requests.get(f'{ENDPOINT}/api/list', headers=header)
    assert response.status_code == 200
    data = response.json()
    return data
