RED = "\u001b[31m"
GREEN = "\u001b[32m"
END = "\u001b[0m"


class Tree:
    def __init__(self):
        self.blobs = []
        self.trees = []


# Create git object model program
class GitObjectModel:

    def __init__(self, author):
        self.author = author
        self.root = None
        self.message = ""
        self.parent = "nil"
        self.committer = self.author

    def commit(self, directory, msg):
        self.root = self.get_structure(directory)
        self.message = msg

    def get_structure(self, directory, node="FOLD_1"):
        tree = Tree()

        for item in directory[node]:
            if item in directory:           # It's a folder
                tree_hash = hash(item)
                next_tree = self.get_structure(directory, item)
                tree.trees.append({tree_hash: next_tree})
            else:                           # It's a file
                item_hash = hash(item)
                tree.blobs.append({item_hash: item})
        return tree

    # DEBUG
    # def traverse(self, fold, directory, indent=""):
    #     color = RED if fold in directory else GREEN
    #     print(color + indent + fold + END)
    #     if fold not in directory:
    #         return
    #     for f in directory[fold]:
    #         self.traverse(f, directory, indent + '\t')


git = GitObjectModel("John Smith")
directory = {"FOLD_1": ["FOLD_2"],
             "FOLD_2": ["file_b", "FOLD_3", "FOLD_4"],
             "FOLD_3": [],
             "FOLD_4": ["file_c", "file_d"]}

git.traverse("FOLD_1", directory, "")
git.commit(directory, "First commit")


# FOLD_1
# 	FOLD_2
# 		file_b
# 		FOLD_3
# 		FOLD_4
# 			file_c
# 			file_d