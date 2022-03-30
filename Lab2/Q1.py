class DTNode:
    """DTree node"""
    def __init__(self, d):
        self.d = d
        self.children = []

    def predict(self, f):
        if callable(self.d):
            i = self.d(f)
            next_node = self.children[i]
            return next_node.predict(f)
        else:
            return self.d


def main():
    # The following (leaf) node will always predict True
    node = DTNode(True)

    # Prediction for the input (True, False):
    print(node.predict((True, False)))

    # Sine it's a leaf node, the input can be anything. It's simply ignored.
    print(node.predict(None))

    t = DTNode(True)
    f = DTNode(False)
    n = DTNode(lambda v: 0 if not v else 1)
    n.children = [t, f]
    #print(n)


    print(n.predict(False))
    print(n.predict(True))

    print('%' * 20)

    a = DTNode('A')
    b = DTNode('B')
    parent = DTNode(lambda x: x[2])
    parent.children = [a, b]

    print(parent.predict((0, 0, 0, 0)))
    print(parent.predict((0, 0, 1, 0)))

    print('#' * 20)

    tt = DTNode(False)
    tf = DTNode(True)
    ft = DTNode(True)
    ff = DTNode(False)
    t = DTNode(lambda v: 0 if v[1] else 1)
    f = DTNode(lambda v: 0 if v[1] else 1)
    t.children = [tt, tf]
    f.children = [ft, ff]
    n = DTNode(lambda v: 0 if v[0] else 1)
    n.children = [t, f]

    print(n.predict((True, True)))
    print(n.predict((True, False)))
    print(n.predict((False, True)))
    print(n.predict((False, False)))


if __name__ == '__main__':
    main()
