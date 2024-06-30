import allure

from checkers.http_checkers import check_status_code_http


@allure.suite('Тесты на проверку метода put v1/account_email')
@allure.sub_suite('Позитивные кейсы')
class TestsPutV1AccountEmail:
    @allure.title('Смена почты пользователя')
    def test_put_v1_account_email(
            self,
            account_helper,
            prepare_user
    ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email
        new_email = prepare_user.email + 'new'

        account_helper.register_new_user(login=login, password=password, email=email)
        token = account_helper.change_email(login=login, password=password, email=new_email)
        with check_status_code_http(403, 'User is inactive. Address the technical support for more details'):
            response = account_helper.user_login(login=login, password=password)
        # assert response.status_code == 403, f'Получен неверный код ответа после неподтвержденной после смены почты, {response.status_code}'

        account_helper.activation_by_token_and_login(token=token)

        response = account_helper.user_login(login=login, password=password)
        # assert response.status_code == 200, 'Пользователь не смог авторизоваться после смены и подтверждения новой почты'
