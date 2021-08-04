# -*- coding: utf-8 -*-

"""
free google translate crawler API

see https://github.com/meetDeveloper/freeDictionaryAPI for document and response
schema.
"""

import json
import requests

class FreeDictionary(object):
    free_dictionary_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/{query}"

    def _encode_endpoint(self, query):
        """
        :type query: str
        :rtype: str
        :return: full api url
        """
        query = "-".join([s for s in query.split(" ") if s.strip()])
        return self.free_dictionary_endpoint.format(query=query)

    def _parse_response(self, html):
        """
        :type html: str
        :rtype: dict
        :return:
        """
        return json.loads(html)

    def get(self, query):
        """
        :type html: str
        :rtype: dict
        :return:
        """
        url = self._encode_endpoint(query)
        html = requests.get(url).text
        response = self._parse_response(html)
        if isinstance(response, dict):
            raise ValueError
        elif isinstance(response, list):
            response = response[0]
        return response

fd = FreeDictionary()

