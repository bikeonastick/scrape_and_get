import scrape
import unittest

class TestScrapeMethods(unittest.TestCase):

    def test_extract_filename(self):
        test_uri = 'https://gzmyu4ma9b-flywheel.netdna-ssl.com/wp-content/uploads/2017/08/more-posts.png'
        result = scrape.extract_filename(test_uri)

        self.assertEqual(result, 'more-posts.png')

if __name__ == '__main__':
    unittest.main()
