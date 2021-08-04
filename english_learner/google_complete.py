# -*- coding: utf-8 -*-

import typing
import requests
import xml.etree.ElementTree as ET


class GoogleComplete(object):
    """
    Google complete API caller and parser.
    """
    google_complete_endpoint = "https://www.google.com/complete/search?output=toolbar&q={query}"

    def _encode_endpoint(self, query):
        """
        :type query: str
        :rtype: str
        :return: full api url
        """
        query = "+".join([s for s in query.split(" ") if s.strip()])
        return self.google_complete_endpoint.format(query=query)

    def _parse_response(self, html):
        """
        :type html: str
        :rtype: typing.List[str]
        :return: list of suggestions
        """
        root = ET.fromstring(html)
        suggestion_list = list()
        for suggestion in root.iter("suggestion"):
            suggestion_list.append(suggestion.attrib["data"])
        return suggestion_list

    def get(self, query):
        """
        :type html: str
        :rtype: typing.List[str]
        :return: list of suggestions
        """
        url = self._encode_endpoint(query)
        html = requests.get(url).text
        suggestion_list = self._parse_response(html)
        return suggestion_list

gc = GoogleComplete()
