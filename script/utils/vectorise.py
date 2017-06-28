#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict as dd
from collections import Counter as ct


def get_vec_label(x_list):
    convert_lab = {"comment": [1, 0, 0, 0], 'deny': [
        0, 1, 0, 0], 'query': [0, 0, 1, 0], 'support': [0, 0, 0, 1]}
    vecs = []
    labels = []
    for rep_twe in x_list:
        vecs.append(rep_twe.get_vector())
        labels.append(convert_lab[rep_twe.get_categorie()])
    return np.array(vecs), np.array(labels)


def vectorise_train(train):
    all_words = set()
    for rep_twe in train:
        all_words.update(rep_twe.get_text())
    all_words = sorted(list(all_words))
    for rep_twe in train:
        vector = np.zeros(len(all_words))
        for word in rep_twe.get_text():
            vector[all_words.index(word)] += 1
        rep_twe.set_vector(vector)
    return train, all_words


def vectorise_test(test, all_words):
    for rep_twe in test:
        vector = np.zeros(len(all_words))
        for word in rep_twe.get_text():
            if word in all_words:
                vector[all_words.index(word)] += 1
        rep_twe.set_vector(np.array(vector))
    return test
