import allure


@allure.suite('Тесты на проверку метода put v1/account_token')
@allure.sub_suite('Позитивные кейсы')
class TestsPutV1AccountToken:
    @allure.title('Актививировать аккаунт пользователя')
    def test_put_v1_account_token(
            self,
            account_helper,
            prepare_user
            ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        account_helper.register_new_user(login=login, password=password, email=email)
        account_helper.user_login(login=login, password=password)
