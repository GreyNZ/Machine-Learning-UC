import collections

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

def partition_by_feature_value(feature_index, dataset):
    """
    :param feature_index: integer (feature index)
    :param dataset: A dataset is a list of pairs (v, c), where v is a feature vector, and c is a classification (label)
    :return: first element is a "separator" function, and the second element is the partitioned dataset
    """
    p = list(set([dataset[j][0][feature_index] for j in range(len(dataset))]))
    map = {p[j]:j for j in range(len(p))}
    partitioned_dataset = [[] for _ in range(len(p))]

    def separator(v):
        return map[v[feature_index]]

    for v, c in dataset:
        i = separator(v)
        append_me = (v, c)
        partitioned_dataset[i].append(append_me)

    return separator, partitioned_dataset

def misclassification(data):
    """
    misclassification is defined as 1 - max(k pk)
    :param data: the datas
    :return: impurity
    """
    impurity = 1 - max(proportion(data))
    return impurity

def proportion(data):
    """
    Calculates the proportion of a datset with a specific classification
    :param data: the datas
    :return: the proportion with selected classification
    """
    labels = list(set([item[1] for item in data]))
    m = [0 for _ in range(len(labels))]
    label_dict = {}
    for label in range(len(labels)):
        label_dict.update({labels[label]:label})
    for i in data:
        m[label_dict[i[1]]] += 1
    return [i / len(data) for i in m]

def get_labels(dataset):
    """
    :param dataset: the datas
    :return: set of labels from dataset
    """
    set_of_labels = []
    for label_index in range(len(dataset)):
        set_of_labels.append(dataset[label_index][1])
    return set(set_of_labels)

def choose_feature(dataset, features):
    """
    :param dataset: the datas
    :param features: list of features
    :return: result, feature, data
    """
    feature_result = None
    data_result = None
    minimum = float('inf')
    for label in features:
        smallest = 0
        feature, partitioned_data = partition_by_feature_value(label, dataset)
        impurities = []
        for impurity in partitioned_data:
            impurities.append(misclassification(impurity))
        for index in range(len(impurities)):
            smallest += (len(partitioned_data[index]) / len(dataset)) * impurities[index]
        if smallest < minimum:
            minimum = smallest
            feature_result = label
            data_result = partitioned_data
    return feature_result, feature, data_result

def most_common_label(data):
    """
    return most common label in dataset
    :param data: dataset
    :return: most common label
    """
    label = collections.Counter([x[1] for x in data]).most_common(1)[0][0]
    return label

def make_decision(index, data):
    """
    :param index: index to check
    :param data: data set
    :return: list of decisions
    """
    listy = []
    for item in data:
        listy.append(item[0][index])
    decisions = list(set(listy))
    return decisions


def train_tree(dataset, criterion, attribute_list=None):
    """
    :param dataset: list of pairs, where the first element in each pair is a feature vector,
                    and the second is a classification.
    :param criterion: function evaluates a dataset for a specific impurity measure
    :param attribute_list: function recursive passing attribute list, empty for first call
    :return: node
    """
    labels = get_labels(dataset)
    common = most_common_label(dataset)
    if attribute_list is None:
        attribute_list = [i for i in range(len(dataset[0][0]))]
    if len(labels) == 1 or not len(attribute_list):
        return DTNode(common)
    else:
        feature_result, _, data_result = choose_feature(dataset, attribute_list)
        outcomes = make_decision(feature_result, dataset)
        node = DTNode(lambda x: outcomes.index(x[feature_result]))
        attribute = [attribute for attribute in attribute_list if attribute != feature_result]
        node.children = [train_tree(data, criterion, attribute) for data in data_result]
        return node






def main():
    dataset = [
        ((True, True), False),
        ((True, False), True),
        ((False, True), True),
        ((False, False), False)
    ]
    t = train_tree(dataset, misclassification)
    print('t:', t)
    print('predict: (True, False) expecting True')
    print(t.predict((True, False)))
    print('predict: (False, False) expecting False')
    print(t.predict((False, False)))

    from pprint import pprint
    dataset = [
      (("a", "x", 2), False),
      (("b", "x", 2), False),
      (("a", "y", 5), True),
    ]
    t = train_tree(dataset, misclassification)
    print('predict a x 2, expecting False')
    print(t.predict(("a", 'x', 2)))
    print('predict a y 5, expecting True')
    print(t.predict(("a", 'y', 5)))
    # print('predict 5')
    # print(t.predict(5))




    dataset = [
        (("Sunny", "Hot", "High", "Weak"), False),
        (("Sunny", "Hot", "High", "Strong"), False),
        (("Overcast", "Hot", "High", "Weak"), True),
        (("Rain", "Mild", "High", "Weak"), True),
        (("Rain", "Cool", "Normal", "Weak"), True),
        (("Rain", "Cool", "Normal", "Strong"), False),
        (("Overcast", "Cool", "Normal", "Strong"), True),
        (("Sunny", "Mild", "High", "Weak"), False),
        (("Sunny", "Cool", "Normal", "Weak"), True),
        (("Rain", "Mild", "Normal", "Weak"), True),
        (("Sunny", "Mild", "Normal", "Strong"), True),
        (("Overcast", "Mild", "High", "Strong"), True),
        (("Overcast", "Hot", "Normal", "Weak"), True),
        (("Rain", "Mild", "High", "Strong"), False)
    ]
    v = train_tree(dataset, misclassification)
    print('t', v)
    print('predicting ("Overcast", "Hot", "Normal", "Weak") expecting True')
    print(v.predict(("Overcast", "Hot", "Normal", "Weak")))
    print('predicting ("Rain", "Mild", "High", "Strong") expecting False')
    print(v.predict(("Rain", "Mild", "High", "Strong")))
    print('wild card')
    print(v.predict(("Rain", "Hot", "High", "Strong")))





def test():
    # dataset = [
    #     ((True, True), False),
    #     ((True, False), True),
    #     ((False, True), True),
    #     ((False, False), False)
    # ]
    # t = train_tree(dataset, misclassification)
    # print(t.predict((True, False)))
    # print(t.predict((False, False)))

    from pprint import pprint

    dataset = []
    with open('car.data', 'r') as f:
        for line in f.readlines():
            features = line.strip().split(",")
            dataset.append((tuple(features[:-1]), features[-1]))
    pprint(dataset[:5])
    t = train_tree(dataset, misclassification)
    print('Predicting ("high", "vhigh", "2", "2", "med", "low") expecting unacc')
    print(t.predict(("high", "vhigh", "2", "2", "med", "low")))


if __name__ == '__main__':
    dataset = [
      ((True, True), False),
      ((True, False), True),
      ((False, True), True),
      ((False, False), False)
    ]
    t = train_tree(dataset, misclassification)
    print(t.predict((True, False)))
    print(t.predict((False, False)))


    dataset = [
        (("Sunny",    "Hot",  "High",   "Weak"),   False),
        (("Sunny",    "Hot",  "High",   "Strong"), False),
        (("Overcast", "Hot",  "High",   "Weak"),   True),
        (("Rain",     "Mild", "High",   "Weak"),   True),
        (("Rain",     "Cool", "Normal", "Weak"),   True),
        (("Rain",     "Cool", "Normal", "Strong"), False),
        (("Overcast", "Cool", "Normal", "Strong"), True),
        (("Sunny",    "Mild", "High",   "Weak"),   False),
        (("Sunny",    "Cool", "Normal", "Weak"),   True),
        (("Rain",     "Mild", "Normal", "Weak"),   True),
        (("Sunny",    "Mild", "Normal", "Strong"), True),
        (("Overcast", "Mild", "High",   "Strong"), True),
        (("Overcast", "Hot",  "Normal", "Weak"),   True),
        (("Rain",     "Mild", "High",   "Strong"), False),
    ]
    t = train_tree(dataset, misclassification)
    print(t.predict(("Overcast", "Cool", "Normal", "Strong")))
    print(t.predict(("Sunny", "Cool", "Normal", "Strong")))


    from pprint import pprint

    dataset = []
    with open('car.data', 'r') as f:
        for line in f.readlines():
            features = line.strip().split(",")
            dataset.append((tuple(features[:-1]), features[-1]))
    pprint(dataset[:5])
    t = train_tree(dataset, misclassification)
    print(t.predict(("high", "vhigh", "2", "2", "med", "low")))
