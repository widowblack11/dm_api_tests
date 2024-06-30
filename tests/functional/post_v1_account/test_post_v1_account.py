from datetime import datetime

import pytest
from checkers.http_checkers import check_status_code_http
from checkers.post_v1_account import PostV1Account


def test_post_v1_account(
        account_helper,
        prepare_user
):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    account_helper.register_new_user(login=login, password=password, email=email)
    response = account_helper.user_login(login=login, password=password, validation_response=True)
    PostV1Account.check_response_values(response)


@pytest.mark.parametrize(
    'login, email, password, status_code, error_message', [
        ('1sxasdas', '11sxdqaw2@12.ru', '12345', 400, 'Validation failed'),
        ('1sxasdas', '12%12.ru', '123456', 400, 'Validation failed'),
        ('1', '12@12.ru', '123456', 400, 'Validation failed'),
    ]
)
def test_invalid_data_of_new_user(
        account_helper,
        login,
        email,
        password,
        status_code,
        error_message
):
    with check_status_code_http(status_code, error_message):
        account_helper.register_new_user(login=login, password=password, email=email)
