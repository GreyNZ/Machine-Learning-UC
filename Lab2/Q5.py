class DTNode:
    """DTree node"""
    def __init__(self, d):
        self.data = None
        self.d = d
        self.children = []

    def predict(self, f):
        if callable(self.d):
            i = self.d(f)
            next_node = self.children[i]
            return next_node.predict(f)
        else:
            return self.d
    def leaves(self, next_node=None):
        if not next_node:
            next_node = self
        if len(next_node.children) == 0:
            return 1
        number_of_leaves = 0
        for next_leaf in next_node.children:
            number_of_leaves += self.leaves(next_leaf)
        return number_of_leaves




def main():
    n = DTNode(True)
    print(n.leaves())

    print("################")

    t = DTNode(True)
    f = DTNode(False)
    n = DTNode(lambda v: 0 if not v else 1)
    n.children = [t, f]
    print(n.leaves())


if __name__ == '__main__':
    main()
