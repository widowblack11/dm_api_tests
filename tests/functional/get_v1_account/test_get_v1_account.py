from datetime import datetime

from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http
from dm_api_account.models.user_envelope import UserRoles

from hamcrest import (
    assert_that,
    all_of,
    has_property,
    starts_with,
    has_properties,
    instance_of,
    contains_inanyorder,
    equal_to,
)


def test_get_v1_account_with_auth(
        auth_account_helper
):
    with check_status_code_http():
        response = auth_account_helper.dm_account_api.account_api.get_v1_account()
        GetV1Account.check_get_v1_account(response)


def test_get_v1_account_no_auth(
        account_helper,
        validation_response=False
):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.dm_account_api.account_api.get_v1_account(validation_response=validation_response)
