from datetime import datetime

from assertpy import (
    soft_assertions,
    assert_that,
)

from dm_api_account.models.user_details_envelope import UserRoles


def test_get_v1_account_with_auth_for_soft_assert(
        auth_account_helper
):
    response = auth_account_helper.dm_account_api.account_api.get_v1_account()
    with soft_assertions():
        assert_that(response.resource.login).starts_with('prokopenko')
        assert_that(response.resource.online).is_instance_of(datetime)
        assert_that(response.resource.roles).contains(UserRoles.GUEST, UserRoles.PLAYER)


