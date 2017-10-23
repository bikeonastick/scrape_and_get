import scrape
import unittest
import os
from shutil import rmtree

class TestScrapeMethods(unittest.TestCase):

    def setUp(self):
        self.test_dirname1 = 'test_dir1'
        self.test_dirname_exist = 'test_dir2'
        rmtree(self.test_dirname_exist,True)
        os.mkdir(self.test_dirname_exist)

    def tearDown(self):
        rmtree(self.test_dirname1,True)
        rmtree(self.test_dirname_exist,True)

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

    def test_create_save_directory(self):
        scrape.create_save_directory(self.test_dirname1)
        self.assertTrue(os.path.exists(self.test_dirname1))

    def test_create_save_directory_exists(self):
        """
        Test that create_save_directory works if there is a left over dirty
        directory.
        """
        scrape.create_save_directory(self.test_dirname_exist)
        self.assertTrue(os.path.exists(self.test_dirname_exist))

if __name__ == '__main__':
    unittest.main()
