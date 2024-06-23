def test_put_v1_account_password(
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
