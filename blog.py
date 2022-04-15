from post import Post
class Blog:
    def __init__(self,  title: str,author:str):
        self.posts = []
        self.author = author
        self.title=title

    def __repr__(self):
        return "{} by {} ({} post{})".format(self.title,self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, post: Post):
        self.posts.append(post)

    def json(self):
        return {"author": self.author, "title": self.title, "posts": [post.json() for post in self.posts]}





