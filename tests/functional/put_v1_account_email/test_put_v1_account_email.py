import structlog

from api_mailhog.apis import mailhog_api
from helpers.account_helper import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
from services.api_mailhog import MailHogApi
from services.dm_api_account import DMApiAccount

structlog.configure(
    processors=
    [structlog.processors.JSONRenderer(
        indent=4,
        ensure_ascii=True,
        # sort_keys=True
    )
    ]
)


def test_put_v1_account_email(
        account_helper,
        prepare_user
        ):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    new_email=prepare_user.email + 'new'

    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.change_email(login=login, password=password, email=new_email)
    response = account_helper.user_login(login=login, password=password)
    assert response.status_code == 403, f'Получен неверный код ответа после неподтвержденной после смены почты, {response.status_code}'

    account_helper.activation_by_token_and_login(login=login, email=new_email)

    response = account_helper.user_login(login=login, password=password)
    assert response.status_code == 200, 'Пользователь не смог авторизоваться после смены и подтверждения новой почты'
