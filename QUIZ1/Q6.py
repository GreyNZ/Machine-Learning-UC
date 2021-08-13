#Write a function cea_trace(domains, training_example) that takes a list of domains of input features and a list of training examples for a binary classification problem and returns the traces of the sets S and G.

#Input
#The number of elements in the list domains is equal to the number of features (attributes) in the problem. The i-th element is a collection (set or list with no repetition) of values that can be taken by the i-th feature.

#All the training examples are related to concept learning (binary classification). As such, all the examples are either positive (i.e. True, meaning that they belong to the target concept) or negative (False). Each example is a pair. The first element is a tuple (or a list) with the same length as domains. The i-th element is a value from the domain of the i-th feature. The second element is either True or False indicating a positive or a negative example respectively.

#Output
#The output is a pair (a tuple of length two) of the form (S_trace, G_trace). Each trace is a list containing the snapshots of S or G during the execution of the algorithm. The traces must include the initial values of S and G. The i-th elements are, respectively, the set S or G after processing the i-th training example. Thus the length of each list is len(training_examples) + 1.

#The elements of S and G must be distinct hypotheses. The test cases will not check the type or correctness of the hypotheses in S or G; only the number of them will be checked. This is so that you have freedom in implementing the code/hypothesis objects and their behaviour.

import copy

# If you wish, you can use the following template.
#
# Representation-dependent functions are defined outside of the main CEA
# function. This allows CEA to be representation-independent. In other words
# by defining the following functions appropriately, you can make CEA work with
# any representation.



def decode(code):
    """Takes a code and returns the corresponding hypothesis."""
    def h(x):
        #raise NotImplementedError # Remove this line
        # Complete this function for the conjunction of constraings
        return all(
                    [code[i] != '0' and (code[i] == x[i] or code[i] == '?')
                    for i in range(len(code))]
        )
    return h


def match(code, x):
    """Takes a code and returns True if the corresponding hypothesis returns
    True (positive) for the given input."""
    return decode(code)(x)


def lge(code_a, code_b):
    """Takes two codes and returns True if code_a is less general or equal
    to code_b.
    supp(a) is subset of supp(b)
    """
    # Complete this for the conjunction of constraints. You do not need to
    # decode the given codes.
    result = list()
    for i, j in zip(code_a, code_b):
        if i == '?' or (i != "0" and (i == j or j == "0")):
            result.append(True)
        else:
            result.append(False)
    return not all(result)

def more_general(S, s):
    found = []
    for x in S:
        found.append(lge(s, x))  
    return any(found)

def initial_S(domains):
    """Takes a list of domains and returns a set where each element is a
    code for the initial members of S."""
    # Return an appropriate set
    s = [('0',) * len(domains)]
    #print(s)
    return set(s)


def initial_G(domains):
    """Takes a list of domains and returns a set where each element is a
    code for the initial members of G."""
    # Return an appropriate set
    g = [('?',) * len(domains)]
    #print(g_set)
    return set(g)


def minimal_generalisations(code, x):
    """Takes a code (corresponding to a hypothesis) and returns the set of all
    codes that are the minimal generalisations of the given code with respect
    to the given input x."""
    # Return an appropriate set 
    minimal = list(code)
    for i, c in enumerate(code):
        if c == '0':
            minimal[i] = x[i]
        elif c != x[i]:
            minimal[i] = '?'
    return tuple(minimal)


def minimal_specialisations(cc, domains, x):
    """Takes a code (corresponding to a hypothesis) and returns the set of all
    codes that are the minimal specialisions of the given code with respect
    to the given input x."""
    # Return an appropriate set
    hypothesis_set = []
    for i, c in enumerate(cc):
        if c == '?':
            for domain in domains[i]:
                if domain != x[i]:
                    hypothesis_set.append(cc[:i] + (domain,) + cc[i + 1:])
                elif '0' != c:
                    hypothesis_set.append(cc[:i] + ('0',) + cc[i + 1:])
    return hypothesis_set


def cea_trace(domains, training_example):
    """
    cea_trace(domains, training_example)
    param: domains, list of domains of input features
    param: training_example, list of training examples for a binary classification problem
    return: traces of the sets S and G
    """
    S_trace, G_trace = [], []
    S = initial_S(domains)
    G = initial_G(domains)
    G_trace.append(copy.deepcopy(G))
    S_trace.append(copy.deepcopy(S))
    #For each training example, d, do:
    #  If d is a positive example then:
    #    Remove from G any hypotheses that do not match d
    #    For each hypothesis s in S that does not match d
    #      Remove s from S
    #      Add to S all minimal generalizations, h, of s such that:
    #        1) h matches d
    #        2) some member of G is more general than h
    #    Remove from S any h that is more general than another hypothesis in S
    for x, y in training_example:
        if len(x) == 0:
            break
        if y: # If d is a positive example then:
            for s in copy.deepcopy(S): # For each hypothesis s in S that does not match d
                if not match(s, x):
                    S.discard(s) # Remove s from S
                    if match(minimal_generalisations(s, x), x):
                        for g in G:
                            if lge(minimal_generalisations(s, x), g): 
                                S.add(minimal_generalisations(s, x))
                    for s in copy.deepcopy(S):
                        if more_general(S, s):
                            S.discard(s)
            for g in copy.deepcopy(G):
                if not match(g,x):
                    G.discard(g)
        #If d is a negative example then:
        #    Remove from S any hypotheses that match d
        #    For each hypothesis g in G that matches d
        #        Remove g from G
        #        Add to G all minimal specializations, h, of g such that:
        #            1) h does not match d
        #            2) some member of S is more specific than h
        #    Remove from G any h that is more specific than another hypothesis in G   
        else: # If d is a negative example then:
            for s in copy.deepcopy(S):
                if match(s, x): # Remove from S any hypotheses that match d
                    S.discard(s)
            for g in copy.deepcopy(G):
                if match(g, x): 
                    G.discard(g) # Remove g from G
                    for h in minimal_specialisations(g, domains, x): # Add to G all minimal specializations, h, of g such that:
                        if any([not lge(h, s) for s in S]):
                            G.add(h)
            for g in copy.deepcopy(G):
                if any([not lge(h, g) for h in G if g != h]):
                    G.discard(g)
        # Append S and G (or thier copy) to corresponding trace lists
        S_trace.append(copy.deepcopy(S))
        G_trace.append(copy.deepcopy(G))
    return S_trace, G_trace


def main():
    print('Test 1')
    domains = [
        {'red', 'blue'}
    ]

    training_examples = [
        (('red',), True)
    ]

    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace), len(G_trace))
    print(all(type(x) is set for x in S_trace + G_trace))
    S, G = S_trace[-1], G_trace[-1]
    print(len(S), len(G))
    
    print("match\n2 2\nTrue\n1 1\n\n")

    print('Test 2')
    domains = [
        {'T', 'F'}
    ]

    training_examples = []  # no training examples

    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace), len(G_trace))
    S, G = S_trace[-1], G_trace[-1]
    print(len(S), len(G))
    print("match\n1 1\n1 1\n\n")

    print("Test 3")
    domains = [
        ('T', 'F'),
        ('T', 'F'),
    ]

    training_examples = [
        (('F', 'F'), True),
        (('T', 'T'), False),
    ]

    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace), len(G_trace))
    S, G = S_trace[-1], G_trace[-1]
    print(len(S), len(G))
    print("match\n3 3\n1 2\n\n")

    print('Test 4')
    domains = [
        {'red', 'green', 'blue'}
    ]

    training_examples = [
        (('red',), True),
        (('green',), True),
        (('blue',), False),
    ]

    S_trace, G_trace = cea_trace(domains, training_examples)
    S, G = S_trace[-1], G_trace[-1]
    print(len(S) == len(G) == 0)


    domains = [
        {'sunny', 'cloudy', 'rainy'},
        {'warm', 'cold'},
        {'normal', 'high'},
        {'strong', 'weak'},
        {'warm', 'cool'},
        {'same', 'change'},
    ]

    training_examples = [
        (('sunny', 'warm', 'normal', 'strong', 'warm', 'same'), True),
        (('sunny', 'warm', 'high', 'strong', 'warm', 'same'), True),
        (('rainy', 'cold', 'high', 'strong', 'warm', 'change'), False),
        (('sunny', 'warm', 'high', 'strong', 'cool', 'change'), True),
    ]

    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace) == len(G_trace) == 5)
    if len(S_trace) == len(G_trace) == 5:
        print(S_trace, G_trace)
    else:
        print("Incorrect number of snapshots in S_trace of G_trace.")
        
        
    print("\n\nTEST 4")
    domains = [
        {'sunny', 'cloudy', 'rainy'},
        {'warm', 'cold'},
        {'normal', 'high'},
        {'strong', 'weak'},
        {'warm', 'cool'},
        {'same', 'change'},
    ]
    
    training_examples = [
        (('sunny', 'warm', 'normal', 'strong', 'warm', 'same'), True),
        (('sunny', 'warm', 'high', 'strong', 'warm', 'same'), True),
        (('rainy', 'cold', 'high', 'strong', 'warm', 'change'), False),
        (('sunny', 'warm', 'high', 'strong', 'cool', 'change'), True),
    ]
    
    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace) == len(G_trace) == 5)
    if len(S_trace) == len(G_trace) == 5:
        print(len(S_trace))
        print(len(G_trace))
        print(S_trace)
        print(G_trace)
    else:
        print("Incorrect number of snapshots in S_trace of G_trace.")    
    
    print("match\nTrue\nOK")
    
    domains = [{'Y', 'N'} for _ in range(10)]
    
    domains = [{'Y', 'N'} for _ in range(10)]

    def read_training_csv(string):
        examples = []
        for line in string.splitlines():
            *x, label = [value.strip() for value in line.split(',')]
            y = label == '+'
            examples.append((x, y))
        return examples
    
    
    training_examples = read_training_csv("""\
    Y, N, N, N, Y, Y, Y, N, Y, N, -
    N, N, Y, Y, Y, N, Y, Y, Y, N, -
    N, N, Y, N, Y, Y, N, Y, Y, Y, -
    Y, N, Y, N, Y, N, N, N, Y, N, -
    Y, Y, Y, Y, N, Y, Y, Y, Y, N, -
    Y, Y, Y, Y, N, N, Y, N, N, N, -
    Y, N, Y, N, Y, Y, Y, N, Y, N, -
    Y, N, Y, Y, Y, N, N, Y, N, N, -
    N, Y, Y, Y, Y, N, N, Y, Y, Y, -
    Y, Y, Y, N, Y, Y, Y, N, Y, Y, -
    Y, N, N, N, N, Y, N, Y, N, Y, +
    Y, N, N, Y, Y, Y, N, N, Y, Y, +
    N, N, Y, Y, N, N, N, N, Y, N, -
    Y, N, Y, N, Y, Y, N, N, Y, Y, -
    """)
    
    S_trace, G_trace = cea_trace(domains, training_examples)
    print(len(S_trace) == len(G_trace) == 15)
    
    if len(S_trace) == len(G_trace) == 15:
        print(len(S_trace[1]), len(G_trace[1]))
        print(S_trace[1], G_trace[1])
        print("oh shit")
    else:
        print("Incorrect number of snapshots in S_trace or G_trace.")  
        
    print("\n\n\n")
    domains = [
        {'red', 'green', 'blue'}
    ]
    
    training_examples = [
        (('red',), True),
        (('green',), True),
        (('blue',), False),
    ]
    
    S_trace, G_trace = cea_trace(domains, training_examples)
    S, G = S_trace[-1], G_trace[-1]
    print(len(S)==len(G)==0)    
    print(len(S))
    print(len(G))
    print(G)
    print(S_trace)
    print(G_trace)


if __name__ == "__main__":
    main()