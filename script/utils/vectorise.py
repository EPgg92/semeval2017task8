#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tools to vectorise datas."""

import numpy as np


def convert_label_to_map(lab):
    """Convert label to map."""
    convert_lab = {"comment": 0, 'deny': 1, 'query': 2, 'support': 3}
    return convert_lab[lab]


def convert_map_to_label(mapx):
    """Convert map to label."""
    convert_map = {0: "comment", 1: 'deny', 2: 'query', 3: 'support'}
    return convert_map[mapx]


def vectorise_train(list_tweets):
    """Create with the list of tweet's texts of training a set of vector."""
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
    """Create with the list of tweet's texts of testing a set of vector."""
    test = []
    for rep_twe in list_tweets:
        vector = np.zeros(len(all_words))
        for word in rep_twe:
            if word in all_words:
                vector[all_words.index(word)] += 1
        test.append(vector.tolist())
    return test
