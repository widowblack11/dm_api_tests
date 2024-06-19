
def test_put_v1_account_email(
        account_helper,
        prepare_user
        ):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    new_email=prepare_user.email + 'new'

    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.change_email(login=login, password=password, email=new_email)
    response = account_helper.user_login(login=login, password=password)
    assert response.status_code == 403, f'Получен неверный код ответа после неподтвержденной после смены почты, {response.status_code}'

    account_helper.activation_by_token_and_login(login=login, email=new_email)

    response = account_helper.user_login(login=login, password=password)
    assert response.status_code == 200, 'Пользователь не смог авторизоваться после смены и подтверждения новой почты'
