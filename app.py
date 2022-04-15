blogs: dict = {}


def menu():
    # show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    print_blogs()


def print_blogs():
    # Print available blogs
    for k, v in blogs.items():
        print(f"-{v}")
