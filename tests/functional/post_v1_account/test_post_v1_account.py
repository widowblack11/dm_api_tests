from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
import structlog

structlog.configure(
    processors=
    [structlog.processors.JSONRenderer(
        indent=4,
        ensure_ascii=True,
        #sort_keys=True
    )
     ]
)


def test_post_v1_account():
    # Регистрация пользователя
    account_api = AccountApi(host='http://5.63.153.31:5051')
    login_api = LoginApi(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi(host='http://5.63.153.31:5025')
    login = '8opt3eesfggggg63'
    password = '123345as8'
    email = f'{login}@mail.ru'

    json_data = {
        'login': login,
        'email': email,
        'password': password
    }

    response = account_api.post_v1_account(json_data=json_data)

    assert response.status_code == 201, f'Новый пользователь не был создан, {response.json()}'
    # Получить письма из почтового сервера

    response = mailhog_api.get_api_v2_messages()

    assert response.status_code == 200, 'Письма не были получены'
    # Получить активационный токен
    token = mailhog_api.get_activate_token_by_login(login, response)

    assert token is not None, f'Токен для пользователя {login} не был получен'

    # активация пользователя
    response = account_api.put_v1_account_to_token(token=token)

    assert response.status_code == 200, 'Пользователь не был активирован'
    # авторизация
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True
    }

    response = login_api.post_v1_account_login(json_data=json_data)

    assert response.status_code == 200, 'Пользователь не смог авторизоваться'
