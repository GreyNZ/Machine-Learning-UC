from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                 "true_positive false_negative"
                                 "false_positive true_negative")):
    pass


def roc_non_dominated(classifiers):
    """
    Takes a collection of classifiers and returns only those classifiers that are not dominated by any other classifier in the collection.
    A classifier is represented as a pair (classifier_name, confusion_matrix), where classifier_name is a string
    Aconfusion_matrix is a named tuple representing the two-by-two classification confusion matrix
    Domination is definded by smaller False positve and larger True positve
    """
    doms = []
    print(classifiers[0])
    for color, matrix in classifiers:
      dominant = True
      for color_compare, matrix_compare in classifiers:
        if matrix.true_positive < matrix_compare.true_positive:
          if matrix.false_positive > matrix_compare.false_positive:
            dominant = False
            break
      if dominant:
        doms.append((color, matrix))
    return doms





# Example similar to the lecture notes

classifiers = [
    ("Red", ConfusionMatrix(60, 40,
                            20, 80)),
    ("Green", ConfusionMatrix(40, 60,
                              30, 70)),
    ("Blue", ConfusionMatrix(80, 20,
                             50, 50)),
]
print(sorted(label for (label, _) in roc_non_dominated(classifiers)))
