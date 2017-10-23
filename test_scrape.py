import scrape
import unittest

class TestScrapeMethods(unittest.TestCase):

    def test_extract_filename(self):
        test_uri ='https://gzmyu4ma9b-flywheel.netdna-ssl.com/wp-content/uploads/2017/08/more-posts.png'
        result = scrape.extract_filename(test_uri)
        self.assertEqual(result, 'more-posts.png')

    def test_get_image_uris_from_line_with_one_img(self):
        test_line='<li><img class="foo" src="1.png"></img></li>'
        result = scrape.get_image_uris_from_line(test_line)
        self.assertEqual(len(result),1)

    def test_get_image_uris_from_line_with_two_img(self):
        test_line='<li><img class="foo" src="1.png"></img><img src="2.jpg"></img></li>'
        result = scrape.get_image_uris_from_line(test_line)
        self.assertEqual(len(result),2)

if __name__ == '__main__':
    unittest.main()
