import allure


@allure.suite('Тесты на проверку метода delete v1/account_login_all')
@allure.sub_suite('Позитивные кейсы')
class TestsDeleteV1AccountLoginAll:
    @allure.title('Разлогин пользователя со всех устройств')
    def test_delete_v1_account_all(
            self,
            auth_account_helper
    ):
        response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login_all()
        assert response.status_code == 204, 'Неудачная попытка авторизации'