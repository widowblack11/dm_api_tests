import requests


def test_post_v1_account():
    # Регистрация пользователя

    login = 'optest2'
    password = '12345as'
    email = f'{login}@mail.ru'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }
    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)
    # Получить письма из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    # Получить активационный токен
    # активация пользователя

    response = requests.put('http://5.63.153.31:5051/v1/account/220bba1d-2ab8-43ca-a955-72fe70f51ee5')
    print(response.status_code)
    print(response.text)

    # авторизация

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
