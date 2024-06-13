import structlog
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
structlog.configure(
    processors=
    [structlog.processors.JSONRenderer(
        indent=4,
        ensure_ascii=True,
        #sort_keys=True
    )
     ]
)



def test_put_v1_account_email():
    # Регистрация пользователя
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account_api = AccountApi(configuration=dm_api_configuration)
    login_api = LoginApi(configuration=dm_api_configuration)
    mailhog_api = MailhogApi(configuration=mailhog_configuration)
    login = 'op3e8475135'
    password = '12263345as'
    email = f'{login}@mail.ru'
    new_email = f'{login}new@mail.ru'

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
    token = mailhog_api.get_activate_token_by_login(login, email, response)
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
    # Смена почты
    json_data = {
        'login': login,
        'password': password,
        'email': new_email
    }
    response = account_api.put_v1_account_email(json_data=json_data)
    assert response.status_code == 200, 'Пользователь не смог сменить почту'
    # авторизация
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 403, f'Получен неверный код ответа после неподтвержденной после смены почты, {response.status_code}'

    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, 'Письма не были получены'

    token = mailhog_api.get_activate_token_by_login(login, new_email, response)
    assert token is not None, f'Токен для пользователя {login} не был получен'

    response = account_api.put_v1_account_to_token(token=token)
    assert response.status_code == 200, 'Пользователь не был активирован'

    # авторизация
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 200, 'Пользователь не смог авторизоваться после смены и подтверждения новой почты'
