import euler
import unittest
import mock

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



    def test_getProblemStatement(self):
        self.e.getProblemStatement(1)


