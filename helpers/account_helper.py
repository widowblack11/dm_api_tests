import time
from json import loads

from services.api_mailhog import MailHogApi
from services.dm_api_account import DMApiAccount


def retrier(
        function
):
    def wrapper(
            *args,
            **kwargs
    ):
        token = None
        count = 0
        while token is None:
            response = function(*args, **kwargs)
            return response
            print(f'Попытка получения токена №{count}!')
            count += 1
            if count == 5:
                raise AssertionError('Превышено количество попыток получения активационного токена!')
            if token:
                return token
            time.sleep(1)

    return wrapper


class AccountHelper:
    def __init__(
            self,
            dm_account_api: DMApiAccount,
            mailhog: MailHogApi
    ):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    def register_new_user(
            self,
            login: str,
            password: str,
            email: str
    ):
        json_data = {
            'login': login,
            'email': email,
            'password': password
        }

        response = self.dm_account_api.account_api.post_v1_account(json_data=json_data)
        assert response.status_code == 201, f'Новый пользователь не был создан, {response.json()}'

        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, 'Письма не были получены'

        token = self.get_activate_token_by_login(login=login, email=email)
        assert token is not None, f'Токен для пользователя {login} не был получен'

        response = self.dm_account_api.account_api.put_v1_account_to_token(token=token)
        assert response.status_code == 200, 'Пользователь не был активирован'

        return response

    def user_login(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me
        }
        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)

        return response

    def change_email(
            self,
            login: str,
            password: str,
            email: str
    ):
        json_data = {
            'login': login,
            'password': password,
            'email': email
        }
        response = self.dm_account_api.account_api.put_v1_account_email(json_data=json_data)
        assert response.status_code == 200, 'Пользователь не смог сменить почту'

        return response

    def activation_by_token_and_login(
            self,
            login: str,
            email: str
    ):

        # assert response.status_code == 200, 'Письма не были получены'

        token = self.get_activate_token_by_login(login=login, email=email)
        assert token is not None, f'Токен для пользователя {login} не был получен'

        response = self.dm_account_api.account_api.put_v1_account_to_token(token=token)
        assert response.status_code == 200, 'Пользователь не был активирован'

        return response

    @retrier
    def get_activate_token_by_login(
            self,
            login,
            email
    ):
        token = None
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            find_email = item['Content']['Headers']['To']
            user_login = user_data['Login']
            user_email = ''.join(find_email)
            if user_login == login and user_email == email:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        return token
