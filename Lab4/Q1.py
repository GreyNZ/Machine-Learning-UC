from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                 "true_positive false_negative "
                                 "false_positive true_negative")):

    def __str__(self):
        elements = [self.true_positive, self.false_negative,
                   self.false_positive, self.true_negative]
        return ("{:>{width}} " * 2 + "\n" + "{:>{width}} " * 2).format(
                    *elements, width=max(len(str(e)) for e in elements))

def confusion_matrix(classifier, dataset):
  results = {'tp' : 0, 'fp' : 0, 'tn' : 0, 'fn' : 0,}
  for point, expected in dataset:
    result = classifier(point)
    if result == expected and result:
        results['tp'] += 1
    elif result == expected and not result:
        results['tn'] += 1
    else:
      if result:
        results['fp'] += 1
      else:
        results['fn'] += 1
  return ConfusionMatrix(results['tp'], results['fn'], results['fp'], results['tn'])


dataset = [
    ((0.8, 0.2), 1),
    ((0.4, 0.3), 1),
    ((0.1, 0.35), 0),
]
print(confusion_matrix(lambda x: 1, dataset))
print()
print(confusion_matrix(lambda x: 1 if x[0] + x[1] > 0.5 else 0, dataset))
