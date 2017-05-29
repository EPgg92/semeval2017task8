#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def get_vec_label(x_list):
    vecs = []
    labels = []
    for rep_twe in x_list:
        vecs.append(rep_twe.get_vector())
        labels.append(rep_twe.get_categorie())
    return np.array(vecs), labels


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
        rep_twe.set_vector(vector)
    return test
