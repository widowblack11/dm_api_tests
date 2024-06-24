def test_delete_v1_account(
        auth_account_helper
):
    response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login()
    assert response.status_code == 204, 'Неудачная попытка авторизации'
