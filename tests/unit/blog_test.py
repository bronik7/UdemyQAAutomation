from unittest import TestCase
from blog import Blog
from post import Post
class BlogTest(TestCase):
    def test_crate_blog(self):
        b= Blog("Test title", "Test Author")
        self.assertEqual("Test title", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([],b.posts)

