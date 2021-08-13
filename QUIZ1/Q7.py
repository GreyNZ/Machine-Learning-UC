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




def all_agree(S, G, x):
    """
    Straight from the notes XD
    def predict(VS, x):
    if len(VS) == 0:
        raise ValueError("No hypothesis!")
    if all(h(x) for h in VS):
        return "All positive"
    elif not any(h(x) for h in VS):
        return "All negative"
    else:
        return "positive count:{}, negative count:{}".format(# complete)
    """
    VS = G.union(S)
    if all(decode(s)(x) for s in VS) or not any(decode(s)(x) for s in VS):
        return True
    else:
        return False
    
domains = [
    {'red', 'blue'},
]

training_examples = [
    (('red',), True),
]

S_trace, G_trace = cea_trace(domains, training_examples)
S, G = S_trace[-1], G_trace[-1]
print(all_agree(S, G, ('red',)))
print(all_agree(S, G, ('blue',)))