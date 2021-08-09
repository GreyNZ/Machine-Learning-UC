import itertools

def input_space(domains):
    """
    takes a list of domains of attributes
    returns a collection of all the objects in the input space
    """
    return itertools.product(*domains)


domains = [
{0, 1, 2},
{True, False},
]

for element in sorted(input_space(domains)):
    print(element)
