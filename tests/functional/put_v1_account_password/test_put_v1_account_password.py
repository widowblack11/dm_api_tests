from json import loads

import dm_api_account.apis.account_api


def test_put_v1_account_password(
        account_helper,
        prepare_user,
        account_api,
):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.auth_client(
        login=login,
        password=password
    )
    account_helper.request_reset_password(
        login=login,
        email=email
    )

