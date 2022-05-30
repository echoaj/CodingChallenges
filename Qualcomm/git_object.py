

class Node:
    def __init__(self):
        self.blob = None
        self.tree = None

    def get_hash(self):
        hash_object = hash(self)
        hash_string = str(hash_object)
        return hash_string


class GitObjectModel:
    def __init__(self, author):
        self.__tree = None
        self.__parent = "Nil"
        self.__author = author
        self.__committer = None
        self.__message = None

    def commit(self, directory, msg, name="root"):
        self.message = msg
        node = self.__get_structure(directory, name)
        hash_ = self.__get_hash()
        self.tree = {hash_: node}

    def __get_structure(self, dir, name):
        node = Node()
        # check if name is a file
        if name not in dir:
            hash_ = hash(name)
            node.blob = {hash_, name}
            return node
        # otherwise name must be a directory
        for f in dir[name]:
            node = self.__get_structure(dir, f)
            hash_ = node.get_hash()
            node.tree = {hash_: node}
        return node

    # create hash function that returns a string
    def __get_hash(self):
        hash_object = hash(self)
        hash_string = str(hash_object)
        return hash_string

    # def display_tree(self):
    #     head = self.tree
    #     print(head.blob)
    #     print(head.tree.blob)
    #     print(head.tree.tree)

    def __str__(self):
        return ""


directory = {"root": ["src", "resources", "tests", "README.md"],
             "src": ["script1.py", "script2.py", "script3.py"],
             "resources": ["packages", "README.md"],
             "tests": ["test1.py"],
             "packages": ["script4.py", "script5.py"]}


git = GitObjectModel(author="John Smith")

git.commit(directory, "first commit")

# git.display_tree()



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

