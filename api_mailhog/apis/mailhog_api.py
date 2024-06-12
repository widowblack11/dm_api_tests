from json import loads

import requests

from restclient.client import RestClient


class MailhogApi(RestClient):
    def get_api_v2_messages(
            self,
            limit=50
    ):
        """
        Get Users emails
        :param limit:
        :return:
        """
        params = {
            'limit': limit
        }
        response = self.get(
            path='/api/v2/messages',
            params=params,
            verify=False
        )
        return response

    def get_activate_token_by_login(
            self,
            login,
            response
    ):
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        return token
