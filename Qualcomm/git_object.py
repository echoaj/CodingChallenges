

class Node:
    def __init__(self):
        self.blob = None
        self.tree = None


class GitObjectModel:
    def __init__(self, author):
        self.tree = None
        self.parent = None
        self.author = author
        self.committer = None

    def commit(self, directory, name="root"):
        self.tree = self.get_structure(directory, name)

    def get_structure(self, dir, name):
        node = Node()
        # check if name is a file
        if name not in dir:
            node.blob = name
            return node
        # otherwise name must be a directory
        for f in dir[name]:
            node.tree = self.get_structure(dir, f)
        return node

    def hash(self, obj):
        pass

    def display_tree(self):
        head = self.tree
        print(head.blob)
        print(head.tree.blob)
        print(head.tree.tree)

    def __hash__(self):
        return self.tree

    def __str__(self):
        return ""


directory = {"root": ["src", "resources", "tests", "README.md"],
             "src": ["script1.py", "script2.py", "script3.py"],
             "resources": ["packages", "README.md"],
             "tests": ["test1.py"],
             "packages": ["script4.py", "script5.py"]}


git = GitObjectModel(author="John Smith")

git.commit(directory)

git.display_tree()


""" FOLDER STRUCTURE """
# root
# 	src
# 		script1.py
# 		script2.py
# 		script3.py
# 	resources
# 		packages
# 			script4.py
# 			script5.py
# 		README.md
# 	tests
# 		test1.py
# 	README.md
