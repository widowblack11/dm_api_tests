def test_get_v1_account_with_auth(
        auth_account_helper
):
    response = auth_account_helper.dm_account_api.account_api.get_v1_account()


def test_get_v1_account_no_auth(
        account_helper,
        validation_response=False
):
    response = account_helper.dm_account_api.account_api.get_v1_account(validation_response=validation_response)
    assert response.status_code == 401, f'Неверный код ошибки запроса без авторизации'
