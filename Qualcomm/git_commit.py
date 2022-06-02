
# Create a git commit class
class GitCommit:
    def __init__(self, author):
        self.tree = None
        self.parent = "nil"
        self.author = author
        self.message = ""

    def commit(self, msg):
        self.message = msg

    # make git commit object hashable
    def __hash__(self):
        string = str(self.tree) + self.parent + self.author + self.message
        return hash(string)

    # make git commit object comparable
    def __eq__(self, other):
        res1 = self.__class__ == other.__class__
        res2 = self.tree == other.tree
        res3 = self.parent == other.parent
        res4 = self.author == other.author
        res5 = self.message == other.message
        return res1 and res2 and res3 and res4 and res5


gc = GitCommit("John Smith")
gc.commit("First commit")
print(hash(gc))
