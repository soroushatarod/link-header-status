import unittest
from link_status import LinkHeaderStatus


class TestHelloTest(unittest.TestCase):

    def test_analyse_headers_returns_true(self):
        menu = LinkHeaderStatus('http://www.example.com', 'we')
        link_to_test = ['http://www.example.com']
        result = menu.get_status_codes_of_links(link_to_test)
        status_returned = next(iter(result.values()))
        self.assertEqual(200, status_returned)

    def test_get_links(self):
        menu = LinkHeaderStatus('http://www.example.com', 'p a')
        result = menu.get_links('http://www.example.com', 'p a')
        self.assertEqual('http://www.iana.org/domains/example', result[0])


if __name__ == '__main__':
    unittest.main()
