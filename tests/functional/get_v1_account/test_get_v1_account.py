from datetime import datetime

import allure

from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http


@allure.suite('Тесты на проверку метода get v1/account')
@allure.sub_suite('Позитивные кейсы')
class TestsGetV1Account:
    @allure.step('Получить данные пользователя')
    def test_get_v1_account_with_auth(
            self,
            auth_account_helper
    ):
        with check_status_code_http():
            response = auth_account_helper.dm_account_api.account_api.get_v1_account()
            GetV1Account.check_get_v1_account(response, start_part_of_login='prokopenko')


@allure.suite('Тесты на проверку метода get v1/account')
@allure.sub_suite('Негативные кейсы')
class TestsGetV1Account:
    @allure.step('Получить данные пользователя без авторизации')
    def test_get_v1_account_no_auth(
            self,
            account_helper,
            validation_response=False
    ):
        with check_status_code_http(401, 'User must be authenticated'):
            account_helper.dm_account_api.account_api.get_v1_account(validation_response=validation_response)
