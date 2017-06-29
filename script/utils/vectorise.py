#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict as dd
from collections import Counter as ct


def convert_label_to_map(lab):
    convert_lab = {"comment": 0, 'deny': 1, 'query': 2, 'support': 3}
    return convert_lab[lab]


def convert_map_to_label(mapx):
    convert_map = {0: "comment", 1: 'deny',
                   2: 'query',  3: 'support'}
    return convert_map[mapx]


def vectorise_train(list_tweets):
    all_words = set()
    for rep_twe in list_tweets:
        all_words.update(rep_twe)
    all_words = sorted(list(all_words))
    train = []
    for rep_twe in list_tweets:
        vector = np.zeros(len(all_words))
        for word in rep_twe:
            vector[all_words.index(word)] += 1
        train.append(vector.tolist())
    return train, all_words


def vectorise_test(list_tweets, all_words):
    test = []
    for rep_twe in list_tweets:
        vector = np.zeros(len(all_words))
        for word in rep_twe:
            if word in all_words:
                vector[all_words.index(word)] += 1
        test.append(vector.tolist())
    return test


def main():

    import preprocess as putils

    def hyp1_pp(str0):
        return putils.lemmatize(putils.tokenise(putils.convert_to_lowercase(str0)))

    a = [hyp1_pp(aa) for aa in ["i like pigs", "i hate pigs", "i like sheeps"]]
    b = [hyp1_pp(aa) for aa in ["i love pigs"]]
    vtr, aw = vectorise_train(a)
    vte = vectorise_test(b, aw)
    print(aw)
    print(a)
    print(vtr)
    print(b)
    print(vte)


if __name__ == '__main__':
    main()
