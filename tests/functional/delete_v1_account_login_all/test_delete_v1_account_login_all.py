def test_delete_v1_account_all(
        auth_account_helper
):
    response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login_all()
    assert response.status_code == 204, 'Неудачная попытка авторизации'