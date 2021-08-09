import itertools
def all_possible_functions(X):
    """
    takes the entire input space (for some problem) and
    returns a set of functions that is F
    """
    X = tuple(X)
    result = set()
    permutations = itertools.product((False,True), repeat=len(X))
    for p in permutations:
        def f(x,p=p):
            return {X[i]:p[i] for i in range(len(X))}[x]
        result.add(f)
    return result


def version_space(H, D):
    """
    :param H: hypothesis
    :param D: training data set
    :return: version space
    """
    result = set()
    for hypoth in H:
        if all([hypoth(x) == y for x, y in D]):
            result.add(hypoth)
    return result



X = {"green", "purple"} # an input space with two elements
D = {("green", True)} # the training data is a subset of X * {True, False}
F = all_possible_functions(X)
H = F # H must be a subset of (or equal to) F

VS = version_space(H, D)

print(len(VS))

for h in VS:
    for x, y in D:
        if h(x) != y:
            print("You have a hypothesis in VS that does not agree with the D!")
            break
    else:
        continue
    break
else:
    print("OK")
