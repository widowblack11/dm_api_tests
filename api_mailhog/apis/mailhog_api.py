import json
from json import loads

import requests


class MailhogApi:
    def __init__(
            self,
            host,
            headers=None
    ):
        self.host = host
        self.headers = headers

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
        response = requests.get(
            url=f'{self.host}/api/v2/messages',
            params=params,
            verify=False
        )
        return response

    def get_activate_token_by_login(
            self,
            login,
            email,
            response
    ):
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            find_email = item['Content']['Headers']['To']
            user_login = user_data['Login']
            user_email=''.join(find_email)
            if user_login == login and user_email == email:

                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        return token
