import euler
import unittest
import mock

CHTML_CONTEN_FOR_PROBLEM1 = '''
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
    def _mock_response(
            self,
            status=200,
            content="CONTENT"):
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
        tests = [
            {
                'desc': 'Positive: Problem url integer',
                'args': [1],
                'expected': 'TestContent'
            },
            {
                'desc': 'Positive: Problem url integer',
                'args': [512],
                'expected': 'TestContent'
            },
            {
                'desc': 'Positive: Problem url string',
                'args': ['1'],
                'expected': 'TestContent'
            },
            {
                'desc': 'Negative: passing None number',
                'args': [None],
                'expected': None
            },
            {
                'desc': 'Negative: passing 0 problem number',
                'args': [0],
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
        res = self.e._getProblemFromHtml(CHTML_CONTEN_FOR_PROBLEM1)
        expected = 'If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.'
        self.assertEqual(expected, res)

    def test_getProblemStatement(self):
        self.e.getProblemStatement(1)


