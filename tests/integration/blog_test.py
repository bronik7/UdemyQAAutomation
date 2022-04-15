from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        b = Blog("Test title", "Test Author")
        p = Post("New Title","New Content")
        b.create_post(p)
        self.assertEqual("New Title",b.posts[0].title)
        self.assertEqual("New Content",b.posts[0].content)

    def test_create_json(self):
        b = Blog("Test title", "Test Author")
        p = Post("New Title","New Content")
        b.create_post(p)
        print(b.json())
        expected= {'author': 'Test Author', 'title': 'Test title',
                   'posts': [{'title': 'New Title', 'content': 'New Content'}]}
        print(expected)
        self.assertEqual(b.json(),expected)
