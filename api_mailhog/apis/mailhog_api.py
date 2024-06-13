import json
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

