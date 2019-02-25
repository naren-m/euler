import requests
from bs4 import BeautifulSoup

class Euler:
    def __init__(self):
        self.baseUrl = 'https://projecteuler.net'
        self.problemUrl = self.baseUrl + '/problem=%s'

    def _generateProblemUrl(self, number):
        if number == None or number == 0 or number == '0':
            return None

        return self.problemUrl % number

    def _getUrlContent(self, number):
        url = self._generateProblemUrl(number)
        if url == None:
            return None

        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            return None

        return r.content


    def _getProblemFromHtml(self, htmlContent):
        if htmlContent in ['None', '']:
            return None

        try:
            soup = BeautifulSoup(htmlContent, 'html.parser')
            ps = soup.select("div p")
            s = [p.getText().replace('\n', '') for p in ps]
            s = ' '.join(s)
        except:
            return None
        s = s if s != '' else None
        return s

    def getProblemStatement(self, number=None):
        content = self._getUrlContent(number)
        return self._getProblemFromHtml(content)


