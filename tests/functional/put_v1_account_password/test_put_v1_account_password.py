import allure


@allure.suite('Тесты на проверку метода put v1/account_password')
@allure.sub_suite('Позитивные кейсы')
class TestsPutV1AccountPassword:
    @allure.title('Сменить пароль')
    def test_put_v1_account_password(
            self,
            account_helper,
            prepare_user
    ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email
        account_helper.register_new_user(login=login, password=password, email=email)
        account_helper.auth_client(
            login=login,
            password=password
        )
        new_password = password + 'test_new'
        account_helper.change_password(login=login, old_password=password, new_password=new_password, email=email)
        account_helper.auth_client(
            login=login,
            password=new_password
        )
