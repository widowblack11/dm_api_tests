import allure


@allure.suite('Тесты на проверку метода Post v1/account_login')
@allure.sub_suite('Позитивные кейсы')
class TestsPostV1AccountLogin:
    @allure.title('Успешная авторизация зарегестрированного пользователя')
    def test_post_v1_account_login(
            self,
            account_helper,
            prepare_user
    ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        account_helper.register_new_user(login=login, password=password, email=email)
        account_helper.user_login(login=login, password=password)
