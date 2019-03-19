import requests
import re
from bs4 import BeautifulSoup


class Euler:
    def __init__(self):
        self._baseUrl = 'https://projecteuler.net'
        self._problemUrl = self._baseUrl + '/problem=%s'

    def _generateProblemUrl(self, number):
        if number == None or number == 0 or number == '0':
            return None

        return self._problemUrl % number

    def _getUrlContent(self, url):
        if url == None:
            return None

        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            return None
        return r.content

    def _getProblemFromHtml(self, htmlContent):
        if htmlContent in [None, '']:
            return None

        soup = BeautifulSoup(htmlContent, 'html.parser')

        probNotAvail = soup.findAll(text=re.compile('Problem not accessible'))
        if len(probNotAvail) > 0:
            return None

        try:
            ps = soup.select("div p")
            s = [p.getText().replace('\n', '') for p in ps]
            s = ' '.join(s)
        except:
            return None

        s = s if s != '' else None

        return s

    def _getProblem(self, number=None):
        response = dict()
        response['url'] = None
        response['description'] = None
        url = self._generateProblemUrl(number)

        if url is None:
            return response

        response['url'] = url
        content = self._getUrlContent(url)
        if content is None:
            return response

        response['description'] = self._getProblemFromHtml(content)

        return response

    def problem(self, number=None):
        return self._getProblem(number=number)
