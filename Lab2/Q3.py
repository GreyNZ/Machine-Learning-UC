import math

def misclassification(data):
    """
    misclassification is defined as 1 - max(k pk)
    :param data: the datas
    :return: impurity
    """
    impurity = 1 - max(proportion(data))
    return impurity

def gini(data):
    """
    gini is defined as ∑k pk(1 - pk).
    :param data: the datas
    :return: impurity
    """
    impurity = sum([(1 - p_k) * p_k for p_k in proportion(data)])
    return impurity

def entropy(data):
    """
    entropy is defined as -∑k pk log(pk).
    :param data: the datas
    :return:z impurity
    """
    impurity = -sum([p_k * math.log(p_k) for p_k in proportion(data) if p_k])
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


def main():
    data = [
        ((False, False), False),
        ((False, True), True),
        ((True, False), True),
        ((True, True), False)
    ]
    print("mis {:.4f}".format(misclassification(data)))
    print("gin {:.4f}".format(gini(data)))
    print("ent {:.4f}".format(entropy(data)))

    data = [
        ((0, 1, 2), 1),
        ((0, 2, 1), 2),
        ((1, 0, 2), 1),
        ((1, 2, 0), 3),
        ((2, 0, 1), 3),
        ((2, 1, 0), 3)
    ]
    print("{:.4f}".format(misclassification(data)))
    print("{:.4f}".format(gini(data)))
    print("{:.4f}".format(entropy(data)))

    print('expected 0.5000 0.6111 1.0114')

if __name__ == '__main__':
    main()
