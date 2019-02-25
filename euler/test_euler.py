import euler
import unittest
import mock

HTML_CONTENT_FOR_PROBLEM1 = '''
<!DOCTYPE html>\r\n<html lang="en">\r\n
<head>
</head>
<body>
<h2>Multiples of 3 and 5</h2>
<div id="problem_info">
<h3>Problem 1 <span style="float:right;" class="info noprint">
<span style="left:-400px;width:450px;font-size:80%;">
Published on Friday, 5th October 2001, 06:00 pm; Solved by 827910;
<br />Difficulty rating: 5%</span>
</h3>
</div>
<div class="problem_content" role="problem">
<p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p> <p>Find the sum of all the multiples of 3 or 5 below 1000.</p></div>
</body>
</html>'''


class TestEuler(unittest.TestCase):
    """
    example text that mocks requests.get and
    returns a mock Response object
    """

    def _mock_response(self, status=200, content="CONTENT"):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content

        return mock_resp

    def setUp(self):
        self.e = euler.Euler()
        self.problem1 = 'If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.'
        self.problem2 = '''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

    def test__generateProblemUrl(self):
        tests = [
            {
                'desc': 'Positive: Problem url integer',
                'args': [1],
                'expected': 'https://projecteuler.net/problem=1'
            },
            {
                'desc': 'Positive: Problem url integer',
                'args': [512],
                'expected': 'https://projecteuler.net/problem=512'
            },
            {
                'desc': 'Positive: Problem url string',
                'args': ['1'],
                'expected': 'https://projecteuler.net/problem=1'
            },
            {
                'desc': 'Negative: passing None number',
                'args': [None],
                'expected': None
            },
        ]

        for test in tests:
            with self.subTest(msg=test['desc']):
                res = self.e._generateProblemUrl(test['args'][0])
                self.assertEqual(res, test['expected'], test['desc'])

    @mock.patch('requests.get')
    def test__getUrlContent(self, mock_get):
        baseProbUrl = 'https://projecteuler.net/problem=1',
        tests = [
            {
                'desc': 'Positive: Problem url integer',
                'args': baseProbUrl,
                'expected': 'TestContent'
            },
            {
                'desc': 'Positive: Problem url integer',
                'args': baseProbUrl,
                'expected': 'TestContent'
            },
            {
                'desc': 'Positive: Problem url string',
                'args': baseProbUrl,
                'expected': 'TestContent'
            },
            {
                'desc': 'Negative: passing None Url',
                'args': [None],
                'expected': None
            },
        ]
        mock_resp = self._mock_response(content="TestContent")
        mock_get.return_value = mock_resp

        for test in tests:
            with self.subTest(msg=test['desc']):
                res = self.e._getUrlContent(test['args'][0])
                self.assertEqual(res, test['expected'], test['desc'])

    def test__getProblemFromHtml(self):

        tests = [
            {
                'desc': 'Positive: Hardcoded HTML content for problem 1',
                'args': [HTML_CONTENT_FOR_PROBLEM1],
                'expected': self.problem1
            },
            {
                'desc': 'Positive: Passing actual HTML content for problem 1',
                'args': [self.e._getUrlContent(self.e._generateProblemUrl(1))],
                'expected': self.problem1
            },
            {
                'desc': 'Positive: Passing actual HTML content for problem 2',
                'args': [self.e._getUrlContent(self.e._generateProblemUrl(2))],
                'expected': self.problem2
            },
            {
                'desc': 'Negative: passing None',
                'args': [None],
                'expected': None
            },
            {
                'desc': 'Negative: passing empty string',
                'args': [None],
                'expected': None
            },
            {
                'desc': 'Negative: Invalid html content',
                'args': ['Invlaid html content'],
                'expected': None
            },
        ]

        for test in tests:
            with self.subTest(msg=test['desc']):
                res = self.e._getProblemFromHtml(test['args'][0])
                self.assertEqual(test['expected'], res)

    def test_getProblem(self):
        tests = [
            {
                'desc': 'Positive: Problem url integer',
                'args': [1],
                'expected': ('https://projecteuler.net/problem=1',
                             self.problem1)
            },
            {
                'desc': 'Positive: Problem url integer',
                'args': [2],
                'expected': ('https://projecteuler.net/problem=2',
                             self.problem2)
            },
            {
                'desc': 'Positive: Problem url string',
                'args': ['1'],
                'expected': ('https://projecteuler.net/problem=1',
                             self.problem1)
            },
            {
                'desc': 'Negative: passing None',
                'args': [None],
                'expected': (None, None)
            },
            {
                'desc': 'Negative: passing negative problem number',
                'args': [-1],
                'expected': ('https://projecteuler.net/problem=-1', None)
            },
            {
                'desc': 'Negative: passing non-existant problem number',
                'args': [123456789],
                'expected': ('https://projecteuler.net/problem=123456789',
                             None)
            },
        ]
        for test in tests:
            with self.subTest(msg=test['desc']):
                res = self.e.getProblem(test['args'][0])
                self.assertEqual(test['expected'], res)
