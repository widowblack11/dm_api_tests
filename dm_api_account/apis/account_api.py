import requests

from dm_api_account.models.change_email import ChangeEmail
from dm_api_account.models.registration import Registration
from dm_api_account.models.user_details_envelope import UserDetailsEnvelope
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.client import RestClient


class AccountApi(RestClient):

    def post_v1_account(
            self,
            registration: Registration
    ):
        """
        Register new user
        :return:
        """
        response = self.post(
            path='/v1/account',
            json=registration.model_dump(exclude_none=True, by_alias=True)
        )
        return response

    def get_v1_account(
            self,
            validation_response=True,
            **kwargs

    ):
        """
        Get current user
        :return:
        """
        response = self.get(
            path='/v1/account',
            **kwargs
        )
        if validation_response:
            return UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_to_token(
            self,
            token,
            validation_response=True
    ):
        """
        Activate registered user
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        if validation_response:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            change_email: ChangeEmail,
            validation_response=True
    ):
        """
        Change registered user email
        :return:
        """
        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path='/v1/account/email',
            headers=headers,
            json=change_email.model_dump(exclude_none=True, by_alias=True)
        )
        if validation_response:
            return UserEnvelope(**response.json())

        return response

    def put_v1_account_password(
            self,
            json_data,
            validation_response=True,
            **kwargs
    ):
        """
        Change registered user password
        :param json_data:
        :return:
        """
        response = self.put(
            path='/v1/account/password',
            json=json_data,
            **kwargs
        )
        if validation_response:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            json_data,
            **kwargs
    ):
        """
        Reset registered user password
        :param json_data:
        :return:
        """
        response = self.post(
            path='/v1/account/password',
            **kwargs,
            json=json_data
        )
        return response
