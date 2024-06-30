import allure


@allure.suite('Тесты на проверку метода delete v1/account_login')
@allure.sub_suite('Позитивные кейсы')
class TestsDeleteV1AccountLogin:
    @allure.step('Выйти из аккаунта для текущего пользователя')
    def test_delete_v1_account(
            self,
            auth_account_helper
    ):
        response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login()
        assert response.status_code == 204, 'Неудачная попытка авторизации'
