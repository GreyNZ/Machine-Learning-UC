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

def main():
    from pprint import pprint
    dataset = [
      ((True, True), False),
      ((True, False), True),
      ((False, True), True),
      ((False, False), False),
    ]
    f, p = partition_by_feature_value(0, dataset)
    pprint(sorted(sorted(partition) for partition in p))

    partition_index = f((True, True))
    # Everything in the "True" partition for feature 0 is true
    print(all(x[0]==True for x,c in p[partition_index]))
    partition_index = f((False, True))
    # Everything in the "False" partition for feature 0 is false
    print(all(x[0]==False for x,c in p[partition_index]))

    from pprint import pprint
    dataset = [
      (("a", "x", 2), False),
      (("b", "x", 2), False),
      (("a", "y", 5), True),
    ]
    f, p = partition_by_feature_value(1, dataset)
    pprint(sorted(sorted(partition) for partition in p))
    partition_index = f(("a", "y", 5))
    print(partition_index)
    # everything in the "y" partition for feature 1 has a y
    print(all(x[1]=="y" for x, c in p[partition_index]))

if __name__ == "__main__":
    main()
