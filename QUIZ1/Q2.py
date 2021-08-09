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





####### zTEST 1
X = {"green", "purple"} # an input space with two elements
F = all_possible_functions(X)

#Let's store the image of each function in F as a tuple
images = set()
for h in F:
    images.add(tuple(h(x) for x in X))

for image in sorted(images):
    print(image)


print('should match the following')
print("(False, False)\n(False, True)\n(True, False)\n(True, True)\n\n\n")



####### TEST 2
X2 = {1, 2, 3}
F2 = all_possible_functions(X2)
print(len(F2))
print("should be 8\n\n\n")


######## TEST 3
X3 = {('red','large'), ('green', 'large'), ('red', 'small'), ('green', 'small')}
F3 = all_possible_functions(X3)

# Let's store the image of each function in F as a tuple
images = set()
for h in F3:
    images.add(tuple(h(x) for x in X3))

for image in sorted(images):
    print(image)


(False, False, False, False)
(False, False, False, True)
(False, False, True, False)
(False, False, True, True)
(False, True, False, False)
(False, True, False, True)
(False, True, True, False)
(False, True, True, True)
(True, False, False, False)
(True, False, False, True)
(True, False, True, False)
(True, False, True, True)
(True, True, False, False)
(True, True, False, True)
(True, True, True, False)
(True, True, True, True)
