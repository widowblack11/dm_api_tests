from datetime import datetime

from hamcrest import (
    has_property,
    all_of,
    assert_that,
    has_properties,
    contains_inanyorder,
    instance_of,
    equal_to,
    starts_with,
)

from dm_api_account.models.user_details_envelope import UserRoles


class GetV1Account:
    @classmethod
    def check_get_v1_account(
            cls,
            response
    ):
        assert_that(
            response, all_of(
                has_property('resource', has_property('login', starts_with("prokopenko"))),
                has_property(
                    'resource', has_property('settings', has_property('colorSchema', equal_to('Modern')))
                ),
                has_property('resource', has_property('registration', instance_of(datetime))),
                has_property('resource', has_property('online', instance_of(datetime))),
                has_property(
                    'resource', has_properties(
                        {
                            'roles': contains_inanyorder(
                                UserRoles.PLAYER,
                                UserRoles.GUEST
                            )
                        }
                    )
                )
            )
        )